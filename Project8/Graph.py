import random
import copy


class Graph(object):
	class Edge(object):
		def __init__(self, source, destination, weight):
			"""
			DO NOT EDIT!
			Class representing an Edge in a graph
			:param source: Vertex where this edge originates
			:param destination: Vertex where this edge ends
			:param weight: Value associated with this edge
			"""
			self.source = source
			self.destination = destination
			self.weight = weight
		
		def __eq__(self, other):
			return self.source == other.source and self.destination == other.destination
		
		def __repr__(self):
			return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"
		
		__str__ = __repr__
	
	class Path(object):
		def __init__(self, vertices=list(), weight=0):
			"""
			DO NOT EDIT!
			Class representing a path in a graph
			:param vertices: Ordered list of vertices that compose the path
			:param weight: Total weight of the path
			"""
			self.vertices = vertices
			self.weight = weight
		
		def __eq__(self, other):
			return self.vertices == other.vertices and self.weight == other.weight
		
		def __repr__(self):
			return f"Weight:{self.weight} Path: {' -> '.join([str(v) for v in self.vertices])}\n"
		
		__str__ = __repr__
		
		def add_vertex(self, vertex):
			"""
			Add a vertex id to the path
			:param vertex: id of a vertex
			:return: None
			"""
			self.vertices.append(vertex)
		
		def add_weight(self, weight):
			"""
			Add weight to the path
			:param weight: weight
			:return: None
			"""
			self.weight += weight
		
		def remove_vertex(self):
			"""
			Remove the most recently added vertex from the path
			:return: None
			"""
			if not self.is_empty():
				self.vertices.pop()
		
		def is_empty(self):
			"""
			Check if the path object is empty
			:return: True if empty, False otherwise
			"""
			return len(self.vertices) == 0
	
	class Vertex(object):
		def __init__(self, number):
			"""
			Class representing a vertex in the graph
			:param number: Unique id of this vertex
			"""
			self.edges = []
			self.id = number
			self.visited = False
		
		def __repr__(self):
			"""
			string representation in the console
			:return:
			"""
			return f"Vertex: {self.id}"
		
		__str__ = __repr__
		
		def add_edge(self, destination, weight):
			"""
			Adds a edge into the list of edges for Vertex Class
			:param destination: Vertix object pointing to the next destinaiton vertex
			:param weight: Value
			:return: None
			"""
			self.edges.append(Graph.Edge(self.id, destination, weight))  # adds an edge to list of edges in a vertex
		
		def degree(self):
			"""
			Degree of a vertex
			:return: Degree of the vertex object
			"""
			return len(self.edges)  # returns the degree of the vertex object
		
		def get_edge(self, destination):
			"""
			Gets the edge pointing to the destinaiton vertext
			:param destination:
			:return: edge object
			"""
			for edge in self.edges:
				if edge.destination == destination:  # destination indicate the required edge
					return edge
		
		def get_edges(self):
			"""
			returns the list of edges for the vertex object
			:return:
			"""
			return self.edges  # returns all the edges
	
	def generate_edges(self):
		"""
		DO NOT EDIT THIS METHOD
		Generates directed edges between vertices to form a DAG
		:return: List of edges
		"""
		random.seed(10)
		edges = []
		for i in range(self.size):
			for j in range(i + 1, self.size):
				if random.randrange(0, 100) <= self.connectedness * 100:
					edges.append([i, j, random.randint(-10, 50)])
		return edges
	
	def __init__(self, size=0, connectedness=0):
		"""
		DO NOT EDIT THIS METHOD
		Construct a random DAG
		:param size: Number of vertices
		:param connectedness: Value from 0 - 1 with 1 being a fully connected graph
		"""
		assert connectedness <= 1
		self.adj_map = {}
		self.size = size
		self.connectedness = connectedness
		self.construct_graph()
	
	def construct_graph(self):
		"""
		contruct the graph based on edges generated by generate_edge function
		:return: None
		"""
		edges = self.generate_edges()
		for edge in edges:
			self.insert_edge(edge[0],edge[1],edge[2])  # adds all the edges to graph

		
	def vertex_count(self):
		"""
		:return: The number of vertex in the graph
		"""
		return len(self.adj_map)  # counts the number of vertices in the graph
	
	def vertices(self):
		"""
		:return: Returns the list of vertices in the map
		"""
		return [self.adj_map[i] for i in self.adj_map]  # returns a list of all the vertices in the graph
	
	def insert_edge(self, source, destination, weight):
		"""
		Insert an edge into the graph, with source and destination vertices, and the weight attached to the connection
		:param source: Starting Vertex
		:param destination: Ending Vertex
		:param weight: Value
		:return: None
		"""
		
		if source in self.adj_map:
			edge = self.adj_map[source].get_edge(destination)
			if edge:
				edge.weight = weight  # updates weight if edge relation exist in the graph
			else:
				self.adj_map[source].add_edge(destination, weight)  # if the edge doesn't exist make one
		else:
			vertex = Graph.Vertex(source)  # new vertex object
			vertex.add_edge(destination,weight)  # add edges
			self.adj_map[source] = vertex  # point the ID to the vertex
		if destination not in self.adj_map:
			self.adj_map[destination] = Graph.Vertex(destination)
	
	def find_valid_paths(self, source, destination, limit):
		"""
		Find the list of paths between a source and destination
		:param source: Starting Vertex
		:param destination: Ending Vertex
		:param limit: The weight limit
		:return: List of Pahts
		"""
		vertex = self.adj_map[source]  # initialize all the required objects
		path = Graph.Path()
		path_list = list()
		stack = list()  # stack of vertices
		stack.append(vertex)

		while stack:
		
			if stack[-1].id == destination:  # path complete
				stack[-1].visited = True
				path.add_vertex(stack[-1].id)
				path_deepcopy = copy.deepcopy(path)  # path deep copied
				for i in range(len(path_deepcopy.vertices)-1):
					edge = self.adj_map[path_deepcopy.vertices[i]].get_edge(path_deepcopy.vertices[i+1])
					path_deepcopy.weight += edge.weight  # adds the weight to the deep copied path
				if path_deepcopy.weight <= limit:  # adds to the path list if path weight is less that limit
					path_list.append(path_deepcopy)
					
			if not stack[-1].visited:  # add more vertices to the path
				stack[-1].visited = True
				path.add_vertex(stack[-1].id)
				vertex = stack[-1]
				edges = vertex.get_edges()  # list of all the edges of the last vertex in the stack
				for edge in edges:
					vert_to_add = edge.destination
					vert_to_add = self.adj_map[vert_to_add]  # adds all the vertices

					if not vert_to_add.visited:
						stack.append(vert_to_add)  # adds only the visited vertices
						
			if stack[-1].visited:  # time to pop the stack
				stack[-1].visited = False
				stack.pop()
				path.remove_vertex()
			
		
		return path_list
		
	
	def find_shortest_path(self, source, destination, limit):
		"""
		Find the shortest path between two verteces based on the smallest weight of the path
		:param source: Starting Vertex
		:param destination: Ending Vertex
		:param limit: Weight limit of the path
		:return: path
		"""
		path_list = self.find_valid_paths(source,destination,limit)
		shortest_path = path_list[0]
		for path in path_list:
			if path.weight < shortest_path.weight:  # if path shorter than the shortest known path
				shortest_path = path  # here we go, got a new shorty
		
		return shortest_path  # basically a linear search after we for valid paths
	
	def find_longest_path(self, source, destination, limit):
		"""
		Find the longest path between two verteces based on the smallest weight of the path
		:param source: Starting Vertex
		:param destination: Ending Vertex
		:param limit: Weight limit of the path
		:return: path object
		"""
		path_list = self.find_valid_paths(source, destination, limit)
		
		longest_path = path_list[0]
		for path in path_list:
			if path.weight > longest_path.weight:  # if the path is longer than the longest know path
				longest_path = path  # we got our new lebron james here
		
		return longest_path  # again a linear search
	
	def find_most_vertices_path(self, source, destination, limit):
		"""
		Find the longest path between two verteces based on the smallest weight of the path
		:param source: Starting Vertex
		:param destination: Ending Vertex
		:param limit: Weight limit of the path
		:return: path object
		"""
		path_list = self.find_valid_paths(source, destination, limit)
		most_vert_path = path_list[0]
		for path in path_list:
			if len(most_vert_path.vertices) < len(path.vertices):  # checks for the most number of vertices
				most_vert_path = path  # from the list of valid paths
				
		return most_vert_path
	
	def find_least_vertices_path(self, source, destination, limit):
		"""
		Find the longest path between two verteces based on the smallest weight of the path
		:param source: Starting Vertex
		:param destination: Ending Vertex
		:param limit: Weight limit of the path
		:return: path object
		"""
		path_list = self.find_valid_paths(source, destination, limit)
		least_vert_path = path_list[0]
		for path in path_list:
			if len(least_vert_path.vertices) >= len(path.vertices):  # checks for the most number of vertices and the least weight
				least_vert_path = path  # from the list of valid paths
			
		
		return least_vert_path
