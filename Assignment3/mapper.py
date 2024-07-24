import grpc
import mapreduce_pb2
import mapreduce_pb2_grpc
from concurrent import futures
import os
import sys


MY_ADDRESS = "localhost"
DIRECTORY = ""

class MapperService(mapreduce_pb2_grpc.MapperServiceServicer):
    def __init__(self):
        self.intermediateOutput = []
    
    def map(self,fileName,content,centroids):
        #map having key as index of nearest centroid to which data point belongs and value as the data point:
        mapped_data = []
        content = content.split('\n')
        #convert all data points from string to float:
        for i in range(len(content)):
            if content[i] == '':
                continue
            content[i] = content[i].split(',')
            #print(content[i])
            content[i] = list(map(float,content[i]))
            #print(content[i])
        #centroid list is of form: ['[8.9, 0.2]', '[11.5, -1.9]', '[9.8, 1.2]', ''] now change it to list of floats:
        for i in range(len(centroids)):
            if len(centroids[i]) == 0 or centroids[i].strip() == '':
                continue
            centroids[i] = centroids[i].strip('[]').split(',')
            centroids[i] = [float(coord) for coord in centroids[i]]
        centroids = [centroid for centroid in centroids if centroid]
        #print(content)
        #print(centroids)
        #do it considering our data points are in 2d space
        for data_point in content:
            min_dist = float('inf')
            index = -1
            for i in range(len(centroids)):
                centroid = centroids[i]
                dist = (int(data_point[0])-int(centroid[0]))**2 + (int(data_point[1])-int(centroid[1]))**2
                if dist < min_dist:
                    min_dist = dist
                    index = i
            mapped_data.append((index,data_point))
        #print(mapped_data)
        return mapped_data
    
    
    def performMap(self, request, context):
        if len(request.locations) == 0:#if no data is there to process
            ack = mapreduce_pb2.MapResponse(status = "SUCCESS")
            return ack
        path_input_file = request.locations[0].split("CF")[0]
        path_centroid_file = request.locations[0].split("CF")[1]
        #print(path_input_file)
        #print(path_centroid_file)
        f = open(path_input_file,'r')
        # print(f.read())
        fileName = path_input_file.split('/')
        fileName = fileName[len(fileName)-1]
        #print(f.read().lower())
        centroids = open(path_centroid_file,'r').read().split('\n')
        #print(centroids)
        self.intermediateOutput.extend(self.map(fileName,f.read().lower(),centroids))
        f = open(f"{DIRECTORY}/IntermediateOutput.txt","w")
        for pair in self.intermediateOutput:
            f.write(str(pair))
            f.write('\n')
        f.close()
        ack = mapreduce_pb2.MapResponse(status = "SUCCESS")
        return ack

    def partition(self, request, context):
        R = int(request.R)
        partitions = [[] for _ in range(R)]

        for pair in self.intermediateOutput:
            key = pair[0]  # Assuming key is at index 0
            partition_index = hash(key) % R
            partitions[partition_index].append(pair)

        for i, partition in enumerate(partitions):
            with open(f"{DIRECTORY}/PartitionOutput_{i}.txt", "w") as f:
                f.write(f"Partition {i}\n")
                for pair in partition:
                    f.write(str(pair) + '\n')

        return mapreduce_pb2.PartitionResponse(status="SUCCESS")
        
    
    def shuffle(self, request, context):
        ret = []
        with open(f"{DIRECTORY}/PartitionOutput_{request.MyNum}.txt", "r") as f:
            for line in f:
                #dont add string "Partition i" to the list
                if "Partition" in line:
                    #print(line)
                    continue
                ret.append(line.strip())
        ShuffleResponse = mapreduce_pb2.ShuffleResponse(pairs=ret)
        #print(ret)
        return ShuffleResponse

if __name__ == "__main__":
    port = int(sys.argv[1])
    DIRECTORY = f"{os.getcwd()}/mapper{port}"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    mapper = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mapperService = MapperService()
    mapreduce_pb2_grpc.add_MapperServiceServicer_to_server(mapperService,mapper)
    mapper.add_insecure_port(f"{MY_ADDRESS}:{port}")
    mapper.start()
    mapper.wait_for_termination()
