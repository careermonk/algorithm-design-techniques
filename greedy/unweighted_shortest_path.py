from Vertex import *
from Graph import *
from Queue import *

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
for i in ["a", "b", "c", "d", "e"]:
    g.add_vertex(i)

#add edges to the graph - need one for each edge to make them undirected
#since the edges are unweighted, make all cost 1
g.add_edge("a", "b", 1)
g.add_edge("a", "d", 1)
g.add_edge("b", "d", 1)
g.add_edge("b", "e", 1)
g.add_edge("c", "a", 1)
g.add_edge("c", "f", 1)
g.add_edge("d", "f", 1)
g.add_edge("d", "g", 1)
g.add_edge("e", "g", 1)
g.add_edge("g", "f", 1)
unweighted_shortest_path(g, "a") 
