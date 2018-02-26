# store graph in adjacency matrix
from apgl.graph import SparseGraph
import numpy

graph = SparseGraph(10)
# file streaming
file = "testData.txt"
f = open(file, "r")


if f.mode == 'r':
    content = f.readlines()
    print("contents\n",content)
    i = 0
    for line in content:
        data = line.split(" ")
        n1 = int(data[0])
        n2 = int(data[1])
        w = int(data[2])
        graph[n1,n2] = w
    print(graph[0, 5])
else:
    exit()
