#  File: Graph.py
#  Description: This program creates a graph.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 313E
#  Unique Number: 50965
#  Date Created: 05/01/16
#  Date Last Modified: 05/01/16

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited 

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the label
  def __str__(self):
    return str (self.label)

class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight = 1):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    return self.weight < other.weight

  def __le__ (self, other):
    return self.weight <= other.weight

  def __gt__ (self, other):
    return self.weight > other.weight

  def __ge__ (self, other):
    return self.weight >= other.weight

  def __eq__ (self, other):
    return self.weight == other.weight

  def __ne__ (self, other):
    return self.weight != other.weight
  
class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # checks if a vertex label already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # add a vertex with given label
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
    
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # does a depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop() 
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)

    # stack is empty; reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # does a breadth first search in a graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
        
  # get index from vertex label
  def getIndex (self, label):
    if not self.hasVertex(label):
      return -1
      
    for i in range (len(self.Vertices)):
      if self.Vertices[i].label == label:
        return i  

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    weight = self.adjMat[self.getIndex(fromVertexLabel)]\
    [self.getIndex(toVertexLabel)]
    if weight == 0:
    	return -1
    else:
    	return weight
    
  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbors = []
    v = self.getIndex(vertexLabel)
    for i in range (len(self.Vertices)):
      if (self.adjMat[v][i] > 0):
        neighbors.append(self.Vertices[i])
    return neighbors
    
  # get a copy of the list of vertices
  def getVertices (self):
    copy = []
    for v in self.Vertices:
      copy.append(v)
    return copy
    
  # determine if the graph has a cycle
  def hasCycle (self):
    for v in self.Vertices: 
      if self.cycleRecursion(None, v):
        return True
      
      # Reset all flags (all vertices are unvisited)
      for i in range (len(self.Vertices)):
        (self.Vertices[i]).visited = False

    return False
    
  # Helper function for hasCycle()  
  # Recursively checks all neighbors for each vertex
  # Returns true if one of the neighbors of v completes a cycle
  def cycleRecursion(self, previous, v):
    if v.wasVisited() == True:
      return True
      
    v.visited = True
    neighbors = self.getNeighbors(v.label)
    
    # Make sure backtracking is not counted 
    #   or it will be mistaken as completing a cycle
    if previous in neighbors:
      neighbors.remove(previous)
    if len(neighbors) == 0:
      return False
      
    for neighbor in neighbors:
      return self.cycleRecursion(v, neighbor)
  
  # return a list of vertices after a topological sort
  def toposort (self):
    nVerts = len(self.Vertices)
    
    # Make a copy of the Graph
    copyGraph = Graph()
    for v in self.Vertices:
      copyGraph.addVertex(v.label)
    for i in range(nVerts):
      for j in range(nVerts):
        copyGraph.addDirectedEdge(i, j, self.adjMat[i][j])  
    
    # Return empty list if cycle is present
    sorted = []
    if self.hasCycle():
      return sorted
    
    # Go through adjacency matrix until a vertex with no
    #   successor is found. This vertex is then added to the
    #	list "sorted", and deleted from the adjacency matrix.
    #   These steps are repeated until the adj. matrix is empty.
    while nVerts > 0:    
      row = 0
      while row < nVerts:
        for j in range(nVerts):
          if copyGraph.adjMat[row][j] != 0:
            row += 1
            break
            
        # If the row has all zeros, then it is
        #   added to the end of our topological sort list
        if j == nVerts - 1:
          # lastVert should have no successors
          lastVert = copyGraph.Vertices[row]
          sorted.insert(0, lastVert)
          copyGraph.deleteVertex(lastVert.label)
          break
      nVerts -= 1      
      
    return sorted
    
  # prints a list of edges for a minimum cost spanning tree
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  # Uses Prim's algorithm
  def spanTree (self):
    nVerts = len(self.Vertices)
    U = [self.Vertices[0]]	# List of vertices in the MST
    pathLength = 0
    edgesList = []
    
    while len(U) < len(self.Vertices):
    	closestV = []	# List of neighbors to vertices in U
    	lowcostE = []	# Edges between vertices in U and their neighbors
    	# Find the neighbors to vertices in U, and add to 
    	#   closestV and add the edges to lowcostE
    	for v in U:
    		for i in range(nVerts):
    			toVertex = self.Vertices[i]
    			weight = self.adjMat[self.getIndex(v.label)][i]
    			if (weight != 0) and (toVertex not in U):
    				closestV.append(self.Vertices[i])
    				newEdge = Edge(v, toVertex, weight)
    				lowcostE.append(newEdge)
    				
    	# Sort the edges in lowcostE in order of ascending weight
    	lowcostE.sort()
    	newEdge = lowcostE.pop(0)
    	
    	pathLength += newEdge.weight
    	fromV = newEdge.u
    	toV = newEdge.v
    	U.append(toV)
    	edgeString = fromV.label + ' - ' + toV.label
    	edgesList.append(edgeString)
    	
    print("Cost =", pathLength)
    print("\nEdges:")
    for edge in edgesList:
    	print(edge)
  	
  # Uses Dijkstra's algorithm
  def shortestPath (self, fromVertexLabel):
    nVerts = len(self.Vertices)
    currentIdx = self.getIndex(fromVertexLabel)
    current = self.Vertices[currentIdx]
    
    visited = set()
    visited.add(current)
    
    # Each index in distances corresponds to the vertex at that index
    #   in self.Vertices
    # distances[i][0] is the last visited vertex before "to vertex"
    # distances[i][1] is the "to vertex"
    # distances[i][2] is the total distance to vertex i
    distances = []
    for i in range(nVerts):	
    	row = [current, self.Vertices[i], float("inf")]
    	distances.append(row)
    
    while len(visited) < nVerts:
    	for i in range(len(distances)):
    		length = self.adjMat[currentIdx][i]
    		
    		# distSoFar is distance from initial to current vertex
    		if current.label == fromVertexLabel:
    			distSoFar = 0
    		else:
    			distSoFar = distances[currentIdx][2]
    		# See if new path length is shorter than the previously found path
    		if length > 0 and (length + distSoFar) < distances[i][2] \
    		and distances[i][1] not in visited:
    			distances[i][2] = length + distSoFar
    			distances[i][0] = current
    			
    	# Next vertex is the minimum path in distances that is not already used
    	minEdge = distances[0]
    	for i in range(1, len(distances)):
    		if distances[i][2] < minEdge[2] and \
    		distances[i][1] not in visited:
    			minEdge = distances[i]
    			
    	current = minEdge[1]
    	currentIdx = self.getIndex(current.label)
    	visited.add(current)
    		
    # Print shortest paths
    for entry in distances:
    	if not entry[2] == float("inf"):	# Take out initial vertex
    		print("Austin to", entry[1], '-', entry[2], end = '')
    		if entry[0].label != fromVertexLabel:
    			print(" (via", entry[0], '\b)')
    		else:
    			print()
    
  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    start = self.getIndex(fromVertexLabel)
    finish = self.getIndex(toVertexLabel)
    self.adjMat[start][finish] = 0
    
    
  # Delete a vertex from the vertex list and all edges from and
  #   to it in the adjacency matrix.
  # Vertex will still exist in adjMat, but all edge weights 
  #   will be set to zero.
  def deleteVertex (self, vertexLabel):
    v = self.getIndex(vertexLabel)
    nVert = len(self.Vertices)
    
    # Delete the column
    for i in range(nVert):
      for j in range(v, nVert - 1):
        self.adjMat[i][j] = self.adjMat[i][j+1]
      self.adjMat[i].pop()
    
    # Delete the row
    self.adjMat.pop(v)
    
    for vertex in self.Vertices:
      if vertex.label == vertexLabel:
        self.Vertices.remove(vertex)
    
def main():
  # Create Graph object
  cities = Graph()


  # Open file for reading
  inFile = open ("./graph.txt", "r")


  # Read the vertices
  numVertices = int ((inFile.readline()).strip())
  print ("\nNumber of cities:", numVertices, '\n')

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)


  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  print ("\nNumber of edges:", numEdges, '\n')

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    #
    ## COMMENT OUT "WEIGHT" FOR TOPSORT.TXT
    #
    weight = int (edge[2])
    cities.addDirectedEdge (start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()
  print ("\nStarting vertex:", startVertex, '\n')


  # Close file
  inFile.close()
  
    
  # print the adjacency matrix
  nVert = len (cities.adjMat)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()


  # Do depth first search 
  print ("DEPTH FIRST SEARCH FROM", startVertex, '\b:')
  cities.dfs (cities.getIndex(startVertex))
  print()


  # Do breadth first search
  print ("BREADTH FIRST SEARCH FROM", startVertex, '\b:')
  cities.bfs (cities.getIndex(startVertex))
  print()
  
  print("\nGraph has a cycle:", cities.hasCycle())
  print() 
  
  # test topological sort
  print("\nTOPOLOGICAL SORT:")
  sorted = cities.toposort()
  print()
  for v in sorted:
    print(v.label)


  # test minimum cost spanning tree
  print("\nMINIMUM COST SPANNING TREE USING PRIMM'S ALGORITHM:")
  cities.spanTree()


  # test single source shortest path algorithm
  print("\n\nSHORTEST PATHS USING DIJKSTRA'S ALGORITHM:")
  cities.shortestPath(startVertex)
  print()
  
  
  # Test getEdgeWeight() and getVertices()
  print("\nTESTING getEdgeWeight():")
  verticesCopy = cities.getVertices()
  city1 = str(verticesCopy[0])
  city2 = str(verticesCopy[1])
  print(city1, '-', city2, \
	'=', cities.getEdgeWeight(city1, city2), '\n')

  
  # Test deleteEdge()
  print("\nTESTING deleteEdge():")
  print("Delete:", city1, '-', city2)
  print("New adjMat:")
  cities.deleteEdge(city1, city2)
  # print the adjacency matrix
  nVert = len (cities.adjMat)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()
  
  
  # Test deleteVertex()
  print("\nTESTING deleteVertex:")
  print("Delete:", city1, '\b,', city2)
  cities.deleteVertex(city1)
  cities.deleteVertex(city2)
  print("\nNew list of cities:")
  for v in cities.Vertices:
  	print(v.label)
  # print the adjacency matrix
  print("\nNew adjMat:")
  nVert = len (cities.adjMat)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()

main()