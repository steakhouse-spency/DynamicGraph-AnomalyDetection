# store graph in adjacency matrix
from apgl.graph import SparseGraph
import numpy

# file streaming
file = "testData.txt"
f = open(file, "r")

# exit if file not in readmode
if f.mode != 'r':
    exit()

# stream graph text file
content = f.readlines()

# get number of nodes
numNodes = int(content[0])

# create sparse graph with numNodes vertices
graph = SparseGraph(numNodes)

# iterate through every node connection
# store in sparse graph
for line in content[1:]:
    data = line.split(" ")
    n1 = int(data[0])
    n2 = int(data[1])
    w = int(data[2])
    graph[n1,n2] = w
    
print(graph)