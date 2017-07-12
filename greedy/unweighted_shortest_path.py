#This class will implement a vertex for a Graph for the
#unweighted shortest path problem
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.previous = None
        self.distance = None

    def set_previous(self, prev):
        self.previous = prev

    def get_previous(self):
        return self.previous

    def set_distance(self, d):
        self.distance = d

    def get_distance(self):
        return self.distance

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " is connected to: " + str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_vertex_ID(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def get_vertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def add_edge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.add_vertex(f)
        if t not in self.vertList:
            nv = self.add_vertex(t)

        fVert = self.vertList[f]
        tVert = self.vertList[t]

        fVert.add_neighbor(tVert, cost)

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return (iter(self.vertList.values()))

class Queue:    
    def __init__(self):
        '''create an empty FIFO queue'''
        self.queue = []

    def size(self):
        '''return number of items in the queue
        pre: none
        post: returns number of items in the queue'''
        return len(self.queue)

    def enqueue(self, data):
        '''insert data at end of queue
        pre: none
        post: data is added to the queue'''
        self.queue.append(data)

    def front(self):
        '''return first item in queue
        pre: queue is not empty; IndexError is raised if empty
        post: returns first item in the queue'''
        return self.queue[0]

    def dequeue(self):
        '''remove and return first item in queue
        pre: queue is not empty; IndexError is raised if empty
        post: removes and returns first item in the queue'''
        return self.queue.pop(0)


def unweighted_shortest_path(g, s): 
    #Create a queue
    q = Queue()

    #Add source node to queue
    source = g.get_vertex(s)
    source.set_distance(0)
    q.enqueue(source)

    #loop while queue is not empty
    while q.size() != 0:
        v = q.dequeue()

        #loop over vertices adjacent to v
        for w in v.get_connections():
            if w.get_distance() is None:
                w.set_previous(v)
                w.set_distance(1 + v.get_distance())
                q.enqueue(w)

    #loop over all nodes and print their distances
    for v in g:
        print("Node", v.get_vertex_ID(), "with distance", v.get_distance())

#create an empty graph
g = Graph()
    
#add vertices to the graph
for i in ["a", "b", "c", "c", "d", "e"]:
    g.add_vertex(i)

#add edges to the graph - need one for each edge to make them undirected
#since the edges are unweighted, make all cost 1
g.add_edge("a", "b", 1)
g.add_edge("a", "c", 1)
g.add_edge("c", "b", 1)
g.add_edge("b", "e", 1)
g.add_edge("c", "d", 1)
g.add_edge("d", "e", 1)
unweighted_shortest_path(g, "a")            
