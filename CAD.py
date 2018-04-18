from InputGraph import ingest
from Distance import dijkstra
from apgl.graph import SparseGraph
import time
# Input: Vertex set V , edge set E, adjacency matrix sequence At, t = 1, .., T , threshold δ, embedding dimension k
# Output: Anomalous edge sets Et, node sets Vt
# 3: for t in {1, .., T-1} do
# 4: Compute commute time distance ct(i, j) for every pair of nodes vi, vj ∈ V with embedding dimension k using [15]
# 5: end for
# 6: for t in {1, .., T-1} do
# 7: Compute ∆Et(e(i,j)) = |At+1(i, j) − At(i, j)| × |ct+1(i, j) − ct(i, j)| for every pair of nodes vi, vj ∈ V
# 8: Choose anomaly edge set Et as the set of edges S with smallest cardinality |S| such that P e∈E−S ∆Et(e) < δ

# 9: for Edge e(i,j)
# in Et do
# 10: vi ∪ vj → Vt
# 11: end for
# 12: Output anomalous edges Et, anomalous nodes Vt
# 13: end for

def cad(filename):
    
    # set of sequential dynamic graphs
    G = ingest(filename)
    # get number of nodes
    n = G[0].getNumVertices()
    
    # set of node distances for graphs in G
    D = []
    #Distance computation for all graphs
    for g in G:
        # compute (commute time with embedding dimension k) distance Ct(i,j) of every pair of nodes for vi,vj within Vt
        # used shortest path w/dijkstra for now
        D.append(dijkstra(g))
    
    # return("done")

    # get number of nodes
    n = G[0].getNumVertices()
    E = []
    # CAD computation 
    for t in range(0,len(G)-1):
        # locate edge weight and distance graphs
        t1 = G[t]
        t2 = G[t+1]
        d1 = D[t]
        d2 = D[t+1]
        
        # Compute ∆Et(e(i,j)) = |Vt+1(i,j) - Vt(i,j)| * |Ct+1(i,j) - Ct(i,j)|
        # save anomolous nodes/edges and delta
        anomNode = []
        for i in range(n):
            for j in range(i+1,n):
                # print("i:",i, " - j:", j, " - t1: ", t1[i,j], " - t2:", t2[i,j], " - d1: ", d1[i,j] , " - d2:", d2[i,j])
                delta = abs(t2[i,j] - t1[i,j]) * abs(d2[i,j] - d1[i,j])
                if delta:
                    anomNode.append({"nodes" : (i,j), "delta" : delta})
        # add anomolous detections to E
        E.append(anomNode)
        
    return(E)


# adj = E.adjacencyList()
# deltaE = {}
# for i in range(E.getNumVertices()): # i = source
#     deltaE.update({i : dict(zip(adj[0][i],adj[1][i]))}) 
    
        
# names = []

# for i in range(1,9):
#     names.append("b"+str(i))
    
# for i in range(1,10):
#     names.append("r"+str(i))

# for i in deltaE:
#     print(names[i],"(",i,"): ",deltaE[i])
