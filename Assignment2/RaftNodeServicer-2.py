import os
import time
import random
import grpc
from concurrent import futures
import raft_pb2
import raft_pb2_grpc

os.environ['NODE_ID'] = '2'
NODES = [0, 1, 2]  # Example list of node IDs

class LogEntry:
    def __init__(self, term, key=None, value=None):
        self.term = term
        self.key = key
        self.value = value

class RaftNodeServicer(raft_pb2_grpc.RaftNodeServicer):
    def __init__(self, node_id):
        self.node_id = node_id
        self.current_term = 0
        self.voted_for = None
        self.log = [LogEntry(0, "NO-OP")]  # Initialize with NO-OP entry
        self.commit_length = 0
        self.state = 'follower'
        self.leader_id = None
        self.leader_lease = None
        self.votes_received = 0
        self.majority = (len(NODES) // 2) + 1  # Majority of nodes
        self.reset_election_timeout()

    def reset_election_timeout(self):
        self.election_timeout = time.time() + random.uniform(5, 10)

    def start_election(self):
        self.state = 'candidate'
        self.current_term += 1
        self.voted_for = self.node_id
        self.votes_received = 1
        self.majority = (len(NODES) // 2) + 1
        self.reset_election_timeout()

        for node_id in NODES:
            if node_id != self.node_id:
                try:
                    channel = grpc.insecure_channel('127.0.0.1:{}'.format(50053 + node_id))
                    stub = raft_pb2_grpc.RaftNodeStub(channel)
                    request = raft_pb2.RequestVoteArgs(
                        term=self.current_term,
                        candidate_id=self.node_id,
                        last_log_index=len(self.log) - 1,
                        last_log_term=self.log[-1].term if self.log else 0
                    )
                    response = stub.RequestVote(request)
                    if response.term > self.current_term:
                        self.state = 'follower'
                        self.current_term = response.term
                        self.voted_for = None
                        self.reset_election_timeout()
                        return
                    if response.vote_granted:
                        self.votes_received += 1
                        if self.votes_received >= self.majority:
                            self.become_leader()
                except grpc.RpcError as e:
                    print(f"Error connecting to node {node_id}: {e}")
                # Handle the error (e.g., log, retry, etc.)

    def become_leader(self):
        self.state = 'leader'
        self.leader_id = self.node_id
        self.leader_lease = time.time() + 10  # Initial lease duration (10 seconds)
        self.send_heartbeats()

    def send_heartbeats(self):
        while True:
            if self.state != 'leader':
                return
            for node_id in NODES:
                if node_id != self.node_id:
                    channel = grpc.insecure_channel('127.0.0.1:{}'.format(50053 + node_id))
                    stub = raft_pb2_grpc.RaftNodeStub(channel)
                    request = raft_pb2.AppendEntryArgs(
                        term=self.current_term,
                        leader_id=self.node_id,
                        prev_log_index=len(self.log) - 1,
                        prev_log_term=self.log[-1].term if self.log else 0,
                        entries=[],
                        leader_commit=self.commit_length
                    )
                    response = stub.AppendEntry(request)
                    if not response.success:
                        self.state = 'follower'
                        self.leader_id = None
                        return
            time.sleep(10)  # Heartbeat interval (10 seconds)

    def RequestVote(self, request, context):
        print(f"Node {self.node_id} received RequestVote RPC from Node {request.candidate_id}")
        pass

    def AppendEntry(self, request, context):
        if request.term < self.current_term:
            print(f"Node {self.node_id} rejected AppendEntries RPC from Node {request.leader_id}.")
            return raft_pb2.AppendEntryReply(term=self.current_term, success=False)

        self.reset_election_timeout()
        self.leader_id = request.leader_id
        self.leader_lease = time.time() + 2.5

        if request.term > self.current_term:
            self.state = 'follower'
            self.current_term = request.term

        if request.prev_log_index >= len(self.log) or \
                (request.prev_log_index >= 0 and self.log[request.prev_log_index].term != request.prev_log_term):
            print(f"Node {self.node_id} rejected AppendEntries RPC from Node {request.leader_id}.")
            return raft_pb2.AppendEntryReply(term=self.current_term, success=False)

        if request.entries:
            for entry in request.entries:
                if entry.term > self.current_term:
                    self.current_term = entry.term
                if entry.term == self.current_term:
                    self.log.append(entry)
                    print(f"Node {self.node_id} accepted AppendEntries RPC from Node {request.leader_id}.")
            if request.leader_commit > self.commit_length:
                self.commit_length = min(request.leader_commit, len(self.log) - 1)

        return raft_pb2.AppendEntryReply(term=self.current_term, success=True)
    
    def check_election_timeout(self):
        """
        Check if the node's election timeout has elapsed. If yes, start the election process.
        """
        if time.time() > self.election_timeout:
            self.start_election()

    def main_loop(self):
        """
        Main loop for the Raft node. This method should be called periodically.
        """
        self.check_election_timeout()
        # Add more checks or operations here as needed.

    def ServeClient(self, request, context):
        print(f"Node {self.node_id} received a {request.Request} request from a client.")

        operation = request.Request
        if operation.startswith('SET'):
            key, value, term = operation.split()[1:]
            self.log.append(LogEntry(term=int(term), key=key, value=value))
            self.commit_length += 1
            print(f"Node {self.node_id} SET {key} {value} {term}")
            with open(f'logs_node_{self.node_id}/logs.txt', 'a') as f:
                f.write(f'SET {key} {value} {term}\n')
            self.main_loop()
            return raft_pb2.ServeClientReply(Data='', LeaderID=str(self.node_id).encode(), Success=True)

        elif operation.startswith('GET'):
            key = operation.split()[1]
            value = self.read_from_database(key)
            self.main_loop()
            return raft_pb2.ServeClientReply(Data=value, LeaderID=str(self.node_id).encode(), Success=True)
        else:
            self.main_loop()
            return raft_pb2.ServeClientReply(Data='', LeaderID=str(self.node_id).encode(), Success=False)


    def read_from_database(self, key):
        with open(f'logs_node_{self.node_id}/logs.txt', 'r') as f:
            for line in f:
                op, k, value, term = line.strip().split()
                if op == 'SET' and k == key:
                    return value
        return ''

def main():
    node_id = int(os.getenv('NODE_ID'))
    raft_node_servicer = RaftNodeServicer(node_id)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    raft_pb2_grpc.add_RaftNodeServicer_to_server(raft_node_servicer, server)
    server.add_insecure_port('[::]:' + str(50053 + node_id))
    server.start()
    print("Raft node {} started".format(node_id))
    try:
        while True:
            time.sleep(1)  # Adjust the sleep time as needed
            raft_node_servicer.main_loop()  # Call main_loop on the instance
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    main()
