import Heap

class Node:
	"""The node class for a node-pointer implementation of a graph.

	id: the name of the given node
	connectedTo (dictionary of edges)  -- keys: the name of the node pointed to by the edge
									    values: the optional weight on the edge"""
	def __init__(self, id):
		self.id = id
		self.connectedTo = {}

	def _addConnection(self, to_id, weight=1):
		"""Adds an edge pointing from this node to another node. Optional weight."""
		self.connectedTo[to_id] = weight

	def _getNeighbors(self):
		"""Returns the names of the nodes this node is connected to"""
		return self.connectedTo.keys()

	def _getWeight(self, target_node):
		"""Returns the weight of the edge connecting this node to a target node."""
		return self.connectedTo[target_node]

	def _getConnections(self):
		return self.connectedTo.keys()

class Graph:
	"""The graph structure itself.

		nodeList (dictionary) -- keys: key mapping to the node objects themselves
								 values: the nodes being mapped to
		numNodes: the number of nodes in the graph"""

	def __init__(self):
		self.nodeList = {}
		self.numNodes = 0

	def __contains__(self, node):
		return node in self.nodeList
	
	def _addNode(self, id):
		self.numNodes += 1
		newNode = Node(id)
		self.nodeList[id] = newNode
		return newNode

	def addEdge(self, from_id, to_id, weight=1):
		if from_id not in self.nodeList:
			newNode = self.addNode(from_id)
		if to_id not in self.nodeList:
			newNode = self.addNode(to_id)
		self.nodeList[from_id]._addConnection(to_id, weight)

	def getEdges(self, node_id):
		"""Given a node, returns the dictionary containing all edges
			connecting this node to other nodes and their corresponding weights."""
		return self.nodeList[node_id].connectedTo

	def getAllNodes(self):
		return self.nodeList.keys()

	def getAllEdges(self):
		"""Returns a list of tuples with the order:
			(starting node, ending node, weight of edge)."""
		edgeList = []
		for node in self.nodeList.values():
			for connection in node._getConnections():
				edgeList.append((node.id, connection, node.connectedTo[connection]))
		return edgeList

	#In progress
	"""def Dijkstra(self, from_id, to_id):
		distances = Heap.Heap()
		for node in self.getAllNodes():
			distances.add(node, float('inf'))
		return distances"""




def testGraph():
	g = Graph()
	for i in range(6):
		g._addNode(i)
	g.addEdge(0,1,5)
	g.addEdge(0,5,2)
	g.addEdge(1,2,4)
	g.addEdge(2,3,9)
	g.addEdge(3,4,7)
	g.addEdge(3,5,3)
	g.addEdge(4,0,1)
	g.addEdge(5,4,8)
	g.addEdge(5,2,1)
	nodes = g.getAllNodes()
	assert nodes == [0, 1, 2, 3, 4, 5]
	edges = g.getAllEdges()
	assert edges == [(0, 1, 5), (0, 5, 2), (1, 2, 4),
					 (2, 3, 9), (3, 4, 7), (3, 5, 3),
					 (4, 0, 1), (5, 2, 1), (5, 4, 8)]

