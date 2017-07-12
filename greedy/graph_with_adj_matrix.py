class Vertex:
    def __init__(self, node):
        self.id = node
        # Mark all nodes unvisited        
        self.visited = False  

    def add_neighbor(self, neighbor, G):
        G.add_edge(self.id, neighbor)

    def get_connections(self, G):
        return G.adjMatrix[self.id]

    def get_vertex_ID(self):
        return self.id

    def set_vertex_ID(self, id):
        self.id = id

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self, numVertices, cost = 0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices =numVertices
        self.vertices = []
        for i in range(0,numVertices):
		newVertex = Vertex(i)
		self.vertices.append(newVertex)

    def set_vertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
		self.vertices[vtx].set_vertex_ID(id)

    def get_vertex(self, n):
        for vertxin in range(0,self.numVertices):
		if n == self.vertices[vertxin].get_vertex_ID():
		    return vertxin
        return -1

    def add_edge(self, frm, to, cost = 0): 
        if self.get_vertex(frm) != -1 and self.get_vertex(to) != -1:
		self.adjMatrix[self.get_vertex(frm)][self.get_vertex(to)] = cost
		#For directed graph do not add this
		self.adjMatrix[self.get_vertex(to)][self.get_vertex(frm)] = cost  

    def get_vertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
		vertices.append(self.vertices[vertxin].get_vertex_ID())
        return vertices

    def print_matrix(self):
        for u in range(0, self.numVertices):
        	row = []
        	for v in range(0, self.numVertices):
        	    row.append(self.adjMatrix[u][v])
        	print row	

    def get_edges(self):
        edges = []
        for v in range(0,self.numVertices):
    		for u in range(0, self.numVertices):
    		    if self.adjMatrix[u][v] != -1:
    			vid = self.vertices[v].get_vertex_ID()
    			wid = self.vertices[u].get_vertex_ID()
    			edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges

if __name__ == '__main__':
    G = Graph(5)
    G.set_vertex(0,'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    print 'Graph data:'  
    G.add_edge('a', 'e', 10)  
    G.add_edge('a', 'c', 20)
    G.add_edge('c', 'b', 30)
    G.add_edge('b', 'e', 40)
    G.add_edge('e', 'd', 50)
    G.add_edge('f', 'e', 60)
    print G.print_matrix()      
    print G.get_edges()    
