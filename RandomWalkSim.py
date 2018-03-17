from random import *
from InputGraph import ingest   



# Brute force version of random walk of weighted graph
# Return distance of random walk from a -> b
def rwsim(filename,a, b):

    # return 0 if a == b
    if(a==b): return 0
    
    # ingest graph
    g = ingest(filename)
    connections = g.adjacencyList(useWeights=False)[0]
    
    # keeps count of total distance of random walk
    count = 0

    # walk from a -> b
    walk = str(a)
    current = a
    while(current != b):
        #print("current = ", current,,"\nconnections = ", connections[current])

        #simulate random index
        length = len(connections[current])
        randindex = randint(0, length-1)
        
        # get next node
        nextnode = connections[current][randindex]
        #print("index of next = ",nextnode, "\n----------------")
        
        # record count
        count += g[current, nextnode]
        

        # set new node
        current = nextnode
        
        # record sequence
        walk += " --> " + str(current)
        

        
    # while(current != a):
    #     # simulate random walk
    #     length = len(connections[current])
    #     nextnode = randint(0, length-1)
        
    #     # set new node
    #     current = connections[current][nextnode]
    
    # walk from b -> a
    # while(current != a):
    #     print()
    
    return({"total": count, "seq": walk})
