from apgl.graph import SparseGraph

def dijkstra(graph):  
    
    #pre process graph
    adj = graph.adjacencyList()
    connections = adj[0]
    weights = adj[1]
    nvert = graph.getNumVertices()
    nodes = list(range(nvert))
    distances = {}
    for i in range(nvert): # i = source
        distances.update({i : dict(zip(connections[i],weights[i]))}) 
    
    
    
    ct = SparseGraph(nvert)
    for i in range(nvert):
        unvisited = {node: None for node in nodes} #using None as +inf
        visited = {}
        current = i
        currentDistance = 0
        unvisited[current] = currentDistance
        
        while True:
            for neighbour, distance in distances[current].items():
                if neighbour not in unvisited: continue
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
            visited[current] = currentDistance
            if i != current:
                ct[i,current] = currentDistance
            del unvisited[current]
            if not unvisited: break
            candidates = [node for node in unvisited.items() if node[1]]
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return ct