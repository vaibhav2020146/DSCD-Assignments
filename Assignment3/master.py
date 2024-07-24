import grpc
import mapreduce_pb2
import mapreduce_pb2_grpc
import os
import subprocess
import threading
import random
import re
import socket

ACK = 0
M = 0
R = 0
centroids_num = 0
number_of_iterations = 0
centroid_list = []
DIRECTORY = "C:/Users/91991/Desktop/DSCD/Assignment3"

def assignMapperPorts():
    ports = [1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241]
    portsList = [0]*M #initialize the list with M zeros
    for i in range(M):
        portsList[i] = ports[i]#assign the ports to the list
    return portsList

def assignReducerPorts():
    ports = [3211,3212,3213,3214,3215,3216,3217,3218,3219,3219,3220]
    portsList = [0]*R
    for i in range(R):
        portsList[i] = ports[i]
    return portsList

def inputSplit(inpLocation):
    inputList = [0]*M
    for i in range(M):
        inputList[i] = []

    count = 0#initialize count to 0 to keep track of the number of files read
    for file in os.listdir(inpLocation):
        inputList[count%M].append(f"{inpLocation}/{file}")#append the file path to the list
        count += 1
    return inputList

def runSubprocessMap(port):
    subprocess.run(["python","C:/Users/91991/Desktop/DSCD/Assignment3/mapper.py",f"{port}"])#run the mapper.py file with the port number as argument

def startMappers(portsList):
    for i in range(len(portsList)):
        # print(f"i is : {i}")
        x = threading.Thread(target = runSubprocessMap,args = [portsList[i]])#run the subprocess in a thread
        x.start()#start the thread

def runSubprocessReduce(port):
    subprocess.run(["python","C:/Users/91991/Desktop/DSCD/Assignment3/reducer.py",f"{port}"])#run the reducer.py file with the port number as argument
def startReducers(portsList):
    for i in range(len(portsList)):
        x = threading.Thread(target = runSubprocessReduce,args = [portsList[i]])#run the subprocess in a thread
        x.start()
    
def Map(args):
    global ACK
    locations,port = args#unpack the arguments
    channel = grpc.insecure_channel(f"localhost:{port}")#create a channel with the port number
    stub = mapreduce_pb2_grpc.MapperServiceStub(channel)#create a stub
    #add path of centroid file in the locations list
    #print(len(locations))
    if len(locations) !=0:
        locations[0]=locations[0]+"CF"+ "C:/Users/91991/Desktop/DSCD/Assignment3/centroids.txt"
    #print(locations)
    InputLocation = mapreduce_pb2.InputLocation(locations = locations)#create an InputLocation object
    MapResponse = stub.performMap(InputLocation)#call the performMap function
    #add the MapResponse to the dump.txt file
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write(f"MapResponse: {MapResponse.status} \n")
    if(MapResponse.status == "SUCCESS"):
        ACK-=1
        # print(f"SUCCESS FROM {port}")

def performMap(inputList,portsList):
    global ACK
    ACK = M
    for i in range(len(inputList)):
        x = threading.Thread(target = Map,args = ((inputList[i],portsList[i]),))#run the Map function in a thread
        x.start()
    while(True):
        if(ACK == 0):
            break
    #open dump.txt file and write the below message
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write("ALL MAP OPERATIONS DONE \n")
    print("ALL MAP OPERATIONS DONE")
    return

def Partition(args):
    global ACK
    R,port = args
    R = str(R)
    channel = grpc.insecure_channel(f"localhost:{port}")#create a channel with the port number
    stub = mapreduce_pb2_grpc.MapperServiceStub(channel)#create a stub
    PartitionInput = mapreduce_pb2.PartitionInput(R = R)#create a PartitionInput object
    PartitionResponse = stub.partition(PartitionInput)#call the partition function
    #add the PartitionResponse to the dump.txt file
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write(f"PartitionResponse: {PartitionResponse.status} \n")
    if(PartitionResponse.status == "SUCCESS"):
        ACK -=1

def performPartition(portsList):
    global ACK
    ACK = M
    for i in range(M):
        x = threading.Thread(target = Partition,args = ((R,portsList[i]),))#run the Partition function in a thread
        x.start()#start the thread
    while(True):
        if(ACK == 0):
            break
    #open dump.txt file and write the below message
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write("ALL PARTITION OPERATIONS DONE \n")
    print("ALL PARTITION OPERATIONS DONE")
    return

def ShuffleAndSort(args):
    global ACK
    SAndSInput = mapreduce_pb2.SAndSInput(MapPorts = args[0],MyNum = args[1])
    port = args[2]
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = mapreduce_pb2_grpc.ReducerServiceStub(channel)
    SAndSResponse = stub.ShuffleAndSort(SAndSInput)
    #add the SAndSResponse to the dump.txt file
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write(f"SAndSResponse: {SAndSResponse.status} \n")
    if(SAndSResponse.status == "SUCCESS"):
        ACK -=1

def performShuffleAndSort(mapperPortList,reducerPortList):
    global ACK
    ACK = R
    for i in range(R):
        x = threading.Thread(target = ShuffleAndSort,args = ([mapperPortList,i,reducerPortList[i]],))
        x.start()
    while(True):
        if(ACK == 0):
            break
    #open dump.txt file and write the below message
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write("ALL SHUFFLE AND SORT OPERATIONS DONE \n")
    print("ALL SHUFFLE AND SORT OPERATIONS DONE")
    return

def Reduce(args):
    global ACK
    # print(f"CHECK IF PORT: {args}")
    ReduceInput = mapreduce_pb2.ReduceInput()
    port = args
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = mapreduce_pb2_grpc.ReducerServiceStub(channel)
    SAndSResponse = stub.performReduce(ReduceInput)
    #add the SAndSResponse to the dump.txt file
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write(f"ReduceResponse: {SAndSResponse.status} \n")
    if(SAndSResponse.status == "SUCCESS"):
        ACK -= 1

def performReduce(reducerPortList):
    global ACK
    ACK = R
    for i in range(R):
        x = threading.Thread(target = Reduce,args = ((reducerPortList[i]),))
        x.start()
    while(True):
        if(ACK == 0):
            break
    #open dump.txt file and write the below message
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write("ALL REDUCE OPERATIONS DONE \n")
    print("ALL REDUCE OPERATIONS DONE")
    return

#update the centroid list updated by the reducer by reading the output file of the reducer:
def updateCentroids():
    global centroid_list
    new_centroid_list = []
    old_centroid_list = centroid_list[:]
    ports = [3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3219, 3220]

    # Iterate over the ports of the reducers
    for port in ports:
        output_file_path = f"C:/Users/91991/Desktop/DSCD/Assignment3/reducer{port}/output.txt"

        # Check if the output file exists
        if not os.path.exists(output_file_path):
            continue
        
        # Read the output file
        with open(output_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Convert the line to a list of floats
                new_centroid_list.append(line.split('\n')[0].split(','))

    centroid_list = new_centroid_list[:]
    #sort the new centroid list
    new_centroid_list.sort()
    #print(new_centroid_list)
    # File path
    file_path = "C:/Users/91991/Desktop/DSCD/Assignment3/centroids.txt"

    # Check if the file exists
    if os.path.exists(file_path):
        # If the file exists, delete it
        os.remove(file_path)

    # Create a new file with the same name
    with open(file_path, "w") as f:
        for centroid_data in new_centroid_list:
            # Convert centroid_data to string
            centroid_str = str(centroid_data)
            # Split the string to extract the coordinates
            coordinates_str = centroid_data[1].split("[")[1].split("]")[0]
            print(coordinates_str)
            #also get second element of the list
            second_element = re.findall(r'\d+\.\d+', centroid_data[2])
            if second_element:
                second_element = second_element[0]
                print(second_element)
            #combine the two elements to form the new centroid
            new_centroid = f"[{coordinates_str},{second_element}]"
            # Write the new centroid to the file
            f.write(new_centroid + "\n")

    #write new centroids to the file dump.txt
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
        f.write("New Centroids: \n")
        for centroid in new_centroid_list:
            f.write(str(centroid))
            f.write('\n')
    
    #print(old_centroid_list)
    #print(new_centroid_list)
    # Check for convergence
    '''if has_converged(old_centroid_list, new_centroid_list):
        print("Convergence reached. Stopping iterations.")
        return True  # Indicate convergence
    else:
        centroid_list = new_centroid_list  # Update centroid_list with the new centroids
        return False  # Indicate convergence not reached'''
    
def has_converged(old_centroids, new_centroids, threshold=0.0001):
    """Check if the centroids have converged."""
    if len(old_centroids) != len(new_centroids):
        return False
    print("Old and new centroids:")
    #(old_centroids)
    print(old_centroids)
    #converting new_centroids to same format as old_centroids
    coordinates = []
    for centroid in new_centroids:
        for coord_str in centroid:
            matches = re.findall(r'\d+\.\d+', coord_str)
            if matches:
                coordinates.extend(map(float, matches))
    new_centroids = [coordinates[i:i+2] for i in range(0, len(coordinates), 2)]
    print(new_centroids)
    val=0
    #iterate over the old and new centroids and check if the difference is less than the threshold
    for i in range(len(old_centroids)):
        for j in range(len(old_centroids[i])):
            val+=(float(old_centroids[i][j])-float(new_centroids[i][j]))**2
    val = val**0.5
    print(val)
    return val < threshold

'''def releasePorts(portsList):
    for port in portsList:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', port))
        sock.close()'''


if __name__=="__main__":

    inpLocation = "C:/Users/91991/Desktop/DSCD/Assignment3/input"
    M = 3
    R = 5
    centroids_num = 5
    number_of_iterations = 2
    #randomly choosing first centroid from the input data
    centroid_list = []
    with open(inpLocation+"/input1.txt") as f:
        data = f.readlines()
        for i in range(centroids_num):
            #convert the data to float and append to the centroid list
            #covert '0.4,7.2' to list of floats [0.4,7.2]:
            centroid_list.append(list(map(float,data[random.randint(0,len(data)-1)].split(','))))
    print(centroid_list)
    #write the centroids to a file
    with open("C:/Users/91991/Desktop/DSCD/Assignment3/centroids.txt","w") as f:
        for centroid in centroid_list:
            f.write(str(centroid))
            f.write('\n')

    mapperPorts = assignMapperPorts()
    reducerPorts = assignReducerPorts()

    inputList = inputSplit(inpLocation)

    #startMappers(mapperPorts)
    #performMap(inputList,mapperPorts)
    #performPartition(mapperPorts)
    #startReducers(reducerPorts)
    #performShuffleAndSort(mapperPorts,reducerPorts)
    #performReduce(reducerPorts)
    #updateCentroids()
    #run the kmeans algorithm for the number of iterations specified and check if convergence is reached:
    for i in range(number_of_iterations):
        with open("C:/Users/91991/Desktop/DSCD/Assignment3/dump.txt","a") as f:
            f.write(f"Iteration: {i} started \n")
        print(f"Iteration: {i} started")
        startMappers(mapperPorts)
        performMap(inputList,mapperPorts)
        performPartition(mapperPorts)
        startReducers(reducerPorts)
        performShuffleAndSort(mapperPorts,reducerPorts)
        performReduce(reducerPorts)
        updateCentroids()
        #releasePorts(mapperPorts)
        #releasePorts(reducerPorts)
        #if updateCentroids():
            #break  # Stop iterations if convergence is reached
