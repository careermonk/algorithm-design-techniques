import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        # Set distance to infinity for all nodes
        self.distance = sys.maxint

        # Mark all nodes unvisited        
        self.visited = False  

        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_vertex_ID(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.vetexCount = 0

    def __iter__(self):
        return iter(self.vertexList.values())

    def add_vertex(self, node):
        self.vetexCount = self.vetexCount + 1
        newVertex = Vertex(node)
        self.vertexList[node] = newVertex
        return newVertex

    def get_vertex(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vertexList:
            self.add_vertex(frm)
        if to not in self.vertexList:
            self.add_vertex(to)
        self.vertexList[frm].add_neighbor(self.vertexList[to], cost)

        #For directed graph do not add this
        self.vertexList[to].add_neighbor(self.vertexList[frm], cost)

    def get_vertices(self):
        return self.vertexList.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def get_edges(self):
        edges = []
	for v in G:
		for w in v.get_connections():
		    vid = v.get_vertex_ID()
		    wid = w.get_vertex_ID()
		    edges.append((vid, wid, v.get_weight(w)))
	return edges

if __name__ == '__main__':
    G = Graph()
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    G.add_edge('a', 'b', 4)  
    G.add_edge('a', 'c', 1)
    G.add_edge('c', 'b', 2)
    G.add_edge('b', 'e', 4)
    G.add_edge('c', 'd', 4)
    G.add_edge('d', 'e', 4)
    print 'Graph data:'
    print G.get_edges()
