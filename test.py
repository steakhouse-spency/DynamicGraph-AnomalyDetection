import InputGraph
from Distance import dijkstra


G = InputGraph.ingest("cadData.txt")

print(G[0][0,8], G[1][0,8])

# print(dijkstra(graph).adjacencyList())
# count = 0
# for i in d:
#     print(count,i, "\n")
#     count += 1