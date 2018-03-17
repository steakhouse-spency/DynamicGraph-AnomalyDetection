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


# set of sequential dynamic graphs
T = {}

# Distance computation
for t in T:
    # compute (commute time) distance Ct(i,j) of every pair of nodes for vi,vj within Vt
    # use embedding dimension k
    print()
    
# CAD computation    
for t in T:
    # Compute ∆Et
        # for every pair of nodes vi, vj within Vt
        # ∆Et(e(i,j)) = |Vt+1(i,j) - Vt(i,j)| * |Ct+1(i,j) - Ct(i,j)|
        
    # set of anomolous edges in ∆Et(e(i,j))
    E = {}
    
    #set of anomlous nodes
    V = {}
    
    for e in E:
        # get anomlous nodes in E
        print()
    
    # return E and V
    
    
    
        
    
    

    
    
    
