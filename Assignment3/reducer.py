import grpc
import mapreduce_pb2
import mapreduce_pb2_grpc
from concurrent import futures
import os
import sys
import copy
import re


MY_ADDRESS = "localhost"
DIRECTORY = ""

class ReducerService(mapreduce_pb2_grpc.ReducerServiceServicer):
    def __init__(self):
        pass

    def strtotup(self,tup):
        match = re.match(r'\((\d+), \[(.*?)\]\)', tup)
        if match:
            tup0 = int(match.group(1))
            tup1 = [float(coord) for coord in match.group(2).split(',')]
            #print(tup0,tup1)
            return tup0, tup1
        else:
            return None

    def Shuffle(self,port,MyNum):
        # print(port)
        channel = grpc.insecure_channel(f"localhost:{port}")
        stub = mapreduce_pb2_grpc.MapperServiceStub(channel)
        ShuffleInput = mapreduce_pb2.ShuffleInput(MyNum = MyNum)

        ShuffleResponse = stub.shuffle(ShuffleInput)
        ret = []
        for pair in ShuffleResponse.pairs:
            ret.append(self.strtotup(pair))
        return ret

    def ShuffleAndSort(self, request, context):
        self.shuffleData = []
        #print(request)
        for port in request.MapPorts:
            self.shuffleData.extend(self.Shuffle(port,request.MyNum))
        self.shuffleData.sort(key = lambda x:x[0])
        SAndSResponse = mapreduce_pb2.SAndSResponse(status = "SUCCESS")
        return SAndSResponse

    def Reduce(self,key,values):
        # Initialize variables to calculate the sum of coordinates
        sum_x = 0
        sum_y = 0
        count = 0
        # Iterate through each data point (coordinate list) in the values list
        for coords_list in values:
            # If the coordinate is a single float, treat it as the x-coordinate
            if isinstance(coords_list, float):
                sum_x += coords_list
                count += 1
            # If the coordinate is a list or tuple, treat it as a [x, y] pair
            elif isinstance(coords_list, list) or isinstance(coords_list, tuple):
                sum_x += coords_list[0]
                sum_y += coords_list[1]
                count += 1

        # Calculate the new centroid coordinates
        new_centroid_x = sum_x / count
        new_centroid_y = sum_y / count
        # Return the updated centroid
        return (key, [new_centroid_x, new_centroid_y])
    
    def performReduce(self, request, context):
        self.reduceResult = []
        i = 0
        f = open(f"{DIRECTORY}/output.txt", 'w')
        # Iterate through all pairs in self.shuffleData
        while i < len(self.shuffleData):
            curr_key, curr_value = self.shuffleData[i]
            values = [curr_value]
            # Iterate through all pairs with the same key
            while i + 1 < len(self.shuffleData) and curr_key == self.shuffleData[i + 1][0]:
                values.append(self.shuffleData[i + 1][1])
                i += 1
            i += 1

            # Reduce the current key with the list of values
            result = self.Reduce(curr_key, values)
            self.reduceResult.append(result)
            # Write the result to the output file
            f.write(str(result) + '\n')
        f.close()
        return mapreduce_pb2.ReduceResponse(status="SUCCESS")

if __name__ == "__main__":
    port = int(sys.argv[1])
    DIRECTORY = f"{os.getcwd()}/reducer{port}"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    reducer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reducerService = ReducerService()
    mapreduce_pb2_grpc.add_ReducerServiceServicer_to_server(reducerService,reducer)
    reducer.add_insecure_port(f"{MY_ADDRESS}:{port}")
    reducer.start()
    reducer.wait_for_termination()
