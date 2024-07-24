import grpc
import raft_pb2
import raft_pb2_grpc
import time

class RaftClient:
    def __init__(self, node_addresses):
        self.node_addresses = node_addresses
        self.leader_id = None

    def set_leader(self, leader_id):
        self.leader_id = leader_id

    def get_leader(self):
        for node_id, address in self.node_addresses.items():
            channel = grpc.insecure_channel(address)
            stub = raft_pb2_grpc.RaftNodeStub(channel)
            request = raft_pb2.ServeClientArgs(Request="GET LEADER")
            response = stub.ServeClient(request)
            if response.LeaderID != '':
                self.leader_id = int(response.LeaderID)
                return
        self.leader_id = None

    def serve_client(self, request):
        while True:
            if self.leader_id is None:
                self.get_leader()

            if self.leader_id is not None:
                channel = grpc.insecure_channel(self.node_addresses[self.leader_id])
                stub = raft_pb2_grpc.RaftNodeStub(channel)
                response = stub.ServeClient(raft_pb2.ServeClientArgs(Request=request))
                if response.Success:
                    return response.Data
                else:
                    self.leader_id = None
                    print("Failed to execute request. Leader may have changed.")
            else:
                print("No leader found. Waiting for leader election...")
                time.sleep(1)

def main():
    node_addresses = {
        0: 'localhost:50051',
        1: 'localhost:50052',
        2: 'localhost:50053'
    }
    client = RaftClient(node_addresses)
    request = input("Enter GET or SET request: ")
    response = client.serve_client(request)
    print("Response from server:", response)

if __name__ == "__main__":
    main()
