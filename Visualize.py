import matplotlib.pyplot as plt
import networkx as nx
from apgl.graph import SparseGraph

def drawGraph(g):
	# create graph instance
	G=nx.Graph()

	# get node connections
	v = g.adjacencyList()[0]
	w = g.adjacencyList()[1]
	rng = len(v)

	for i in range(rng):
		nodeA = i
		neighb = v[i]
		for j in range(len(neighb)):
			nodeB = neighb[j]
			if nodeA < nodeB:
				G.add_edge(nodeA,nodeB,weight=w[i][j])

 	# positions for all nodes
	pos=nx.spring_layout(G)
	
	# nodes
	nx.draw_networkx_nodes(G,pos,node_size=700)

	# edges
	nx.draw_networkx_edges(G,pos,edgelist=G.edges(data=True), width=6)

	# labels
	nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

	plt.axis('on')
	plt.savefig("weighted_graph.png") # save as png
	plt.show()
