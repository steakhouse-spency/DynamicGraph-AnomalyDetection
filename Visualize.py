import matplotlib.pyplot as plt
import networkx as nx
from apgl.graph import SparseGraph

def drawGraph(g, e, threshold, filename):
	# create graph instance
	G=nx.Graph()

	# get node connections
	v = g.adjacencyList()[0]
	w = g.adjacencyList()[1]
	rng = len(v)

	# add node connections to nx Graph
	for i in range(rng):
		nodeA = i
		neighb = v[i]
		for j in range(len(neighb)):
			nodeB = neighb[j]
			if nodeA < nodeB:
				G.add_edge(nodeA,nodeB,weight=w[i][j])

 	# positions for all nodes
	pos=nx.spring_layout(G, k=2, scale=10.0)
	
	# nodes
	nx.draw_networkx_nodes(G,pos,node_size=150, node_color="#0000d8")
	# edges
	nx.draw_networkx_edges(G,pos,edgelist=G.edges(data=True), width=1)
	# labels
	nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif', font_color="w")
	# plot configs
	plt.axis('off')
	plt.savefig(filename) # save as png
	plt.clf()



	# print anomulous version of graph if any
	if len(e) != 0:

		# create list of edges that are detected as anomalies
		anom = []
		for (u,v,d) in G.edges(data=True):
			nodes = (u,v)
			if nodes in e.keys():
				if e[nodes] > threshold:
					# print(nodes, e[nodes])
					anom.append(nodes)

		# nodes
		nx.draw_networkx_nodes(G,pos,node_size=150, node_color="#0000d8")
		# edges
		nx.draw_networkx_edges(G,pos,edgelist=G.edges(data=True), width=1)
		nx.draw_networkx_edges(G, pos, edgelist=anom, width=3, edge_color="r")
		# labels
		nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif', font_color="w")

		# config
		plt.axis('off')
		plt.savefig(filename+"+1") # save as png
		plt.clf()

