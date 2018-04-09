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
    
    # retrieve meta data
    cadMeta = content[0].split(" ")
    
    # get number of nodes
    numNodes = int(cadMeta[0])
    
    # get number of time sequences
    t = int(cadMeta[1])
    
    # generate t amount of graphs
    G = [] 
    for _ in range(t):
        G.append(SparseGraph(numNodes))

        
    # iterate through every node connection
    # store in sparse graph for specific time sequence
    for line in content[1:]:
        data = line.split(" ")
        n1 = int(data[0])
        n2 = int(data[1])
        w = int(data[2])
        t = int(data[3])
        G[t][n1,n2] = w
        
    return G