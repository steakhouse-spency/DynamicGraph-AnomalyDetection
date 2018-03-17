# Input: module 'ingest' takes filename as single argument
# Process: creates a 'SparseGraph' with node weights provided in text file
# Output: returns a 'SparseGraph' of weighted-undirected graph
#
from apgl.graph import SparseGraph

def ingest(filename):
    f = open(filename, "r")
    
    # exit if file not in readmode
    if f.mode != 'r':
        exit()
    
    # stream graph text file
    content = f.readlines()
    f.close()
    
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
        
    return graph