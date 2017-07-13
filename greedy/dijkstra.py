from Vertex import *
from Graph import *
from PriorityQueue import *

def dijkstra(G, s):

    #create a priority queue
    pq = PriorityQueue()

    #insert all vertices into the priority queue (distance is priority)
    for v in G:
        pq.add(v.get_distance(), v.id)

    #loop while priority queue is not empty
    while not(pq.empty()):
        #remove vertex with smallest distance from priority queue
        t = pq.extract_min()
        v = G.get_vertex(t[1])

        #for each vertex w adjacent to v
        for w in v.get_connections():
            if w.get_distance() > (v.get_distance() + v.get_weight(w)):
                w.set_previous(v)
                w.set_distance(v.get_distance() + v.get_weight(w))

        #loop over all nodes and print their distances
    for v in G:
        print "Node", v.get_vertex_ID(), "with distance", v.get_distance()

# Test Code
#create an empty graph
G = Graph()
    
#add vertices to the graph
for i in ["a", "b", "c", "c", "d", "e"]:
    G.add_vertex(i)

#add edges to the graph - need one for each edge to make them undirected
#since the edges are unweighted, make all cost 1
G.add_edge("a", "b", 1)
G.add_edge("a", "d", 1)
G.add_edge("b", "d", 1)
G.add_edge("b", "e", 1)
G.add_edge("c", "a", 1)
G.add_edge("c", "f", 1)
G.add_edge("d", "f", 1)
G.add_edge("d", "g", 1)
G.add_edge("e", "g", 1)
G.add_edge("g", "f", 1)
#set distance of source to zero
source = G.get_vertex("a")
source.set_distance(0)

#set distance for all other vertices to "infinity"
inf = float("infinity")
for i in ["b", "c", "d", "e", "f", "g"]:
    v = G.get_vertex(i)
    v.set_distance(inf)
dijkstra(G, "a")
