import matplotlib.pyplot as plt
import networkx as nx
from apgl.graph import SparseGraph
import operator


def drawGraph(g, e, threshold, filename):


	plt.figure(figsize=(16,12)) 
	nodeSize = 600
	fontSize = 20

	# create graph instance
	G=nx.Graph()
	# print("G:",G)

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
	pos=nx.spring_layout(G, k=1, iterations=35, scale=100)

	# nodes
	nx.draw_networkx_nodes(G,pos,node_size=nodeSize, node_color="#0000d8")
	
	# edges
	nx.draw_networkx_edges(G,pos,edgelist=G.edges(data=True), width=1, edge_color="black", style="dashed")
	
	# labels
	nx.draw_networkx_labels(G,pos,font_size=fontSize,font_family='sans-serif', font_color="w")
	
	# plot configs
	plt.axis('off')
	plt.savefig(filename) # save as png
	plt.clf()


	# return

	# print anomulous version of graph if any
	if len(e) != 0:

		# create list of edges that are detected as anomalies
		anom = {}
		for (u,v,d) in G.edges(data=True):
			nodes = (u,v)
			if nodes in e.keys():
				if e[nodes] > threshold:
					# print(nodes, e[nodes])
					anom.update({nodes: e[nodes]})



		n = []
		for i in anom.keys():
			n.append(i[0])
			n.append(i[1])

		n = list(set(n))


		# find total network of anomulous activity
		anomEdgelist = []
		anomNodeList = []
		for i in n:
			anomNodeList.append(i)
			neighb = g.adjacencyList()[0][i]
			for j in neighb:
				if i < j:
					anomEdgelist.append((i,j))
				else:
					anomEdgelist.append((j,i))		
				anomNodeList.append(j)			
			# 	nodeB = neighb[j]
			# 	if nodeA < nodeB:
		anomEdgeList = list(set(anomEdgelist))
		anomNodeList = list(set(anomNodeList))





		
		mn = min(anom.values())
		mx = max(anom.values())
		dev = round((mx-mn)/3)

		smallAnom = []
		medAnom = []
		lgAnom = []

		for i in anom:
			if anom[i] <= mn + dev:
				smallAnom.append(i)
			elif anom[i] <= mn +(dev*2):
				medAnom.append(i)
			else:
				lgAnom.append(i)




		# print("total",G.nodes(),"\n")
		# print("anom",n, "\n")
		# delete = list(set(G.nodes()) - set(n))
		# G.remove_nodes_from(delete)




		# nodes
		nx.draw_networkx_nodes(G,pos,nodelist=anomNodeList,node_size=nodeSize, node_color="#0000d8")
		nx.draw_networkx_nodes(G,pos,nodelist=n, node_size=nodeSize, node_color="red")
		# all edges
		# nx.draw_networkx_edges(G,pos,edgelist=G.edges(data=True), width=1)

		# anomlous node non anomulus connectiosn
		nx.draw_networkx_edges(G, pos, edgelist=anomEdgelist, width=1, edge_color="grey", style="dashed")

		# anomalous edges
		nx.draw_networkx_edges(G, pos, edgelist=smallAnom, width=2, edge_color="r")
		nx.draw_networkx_edges(G, pos, edgelist=medAnom, width=3, edge_color="r")
		nx.draw_networkx_edges(G, pos, edgelist=lgAnom, width=4, edge_color="r")

		# labels
		nx.draw_networkx_labels(G,pos,font_size=fontSize,font_family='sans-serif', font_color="w")

		# config




		plt.axis('off')

		sorted_anom = sorted(anom.items(), key=operator.itemgetter(1), reverse=True)
		col_labels = ['Nodes','Score']
		plt.table(cellText=sorted_anom,loc='left', colWidths = [.05]*len(sorted_anom), colLabels=col_labels)

		plt.savefig(filename+"+1") # save as png
		plt.clf()

