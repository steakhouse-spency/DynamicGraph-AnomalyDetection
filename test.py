from CAD import cad
import InputGraph
from Visualize import drawGraph
# from Distance import dijkstra


G = InputGraph.ingest("dblp/graphData.txt")
drawGraph(G[2])


# for i in range(len(G)):
# 	print(list(G[i].adjacencyList()[0][2]), "\n\n")
# print(G[0][0,8], G[1][0,8])

# print(dijkstra(graph).adjacencyList())
# count = 0
# for i in d:
#     print(count,i, "\n")
#     count += 1
# test = cad("cadData.txt")


# test = cad("dblp/graphData.txt")

# for i in test:
# 	for j in i:
# 		if j["delta"] >= 3:
# 			print(j, "\n")
# 	print("\n\n\n")