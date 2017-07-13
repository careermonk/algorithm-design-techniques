from Vertex import *
from Graph import *
from PriorityQueue import *

def dijkstra(G, s):

    #create a priority queue
    pq = PriorityQueue()
    
    #set distance for all other vertices to "infinity"
    inf = float("infinity")
    for i in G.get_vertices():
        v = G.get_vertex(i)
        v.set_distance(inf)
    
    #set distance of source to zero
    source = G.get_vertex(s)
    source.set_distance(0)

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
for i in ["a", "b", "c", "d", "e"]:
    G.add_vertex(i)

#add edges to the graph - need one for each edge to make them undirected
#since the edges are unweighted, make all cost 1
G.add_edge("a", "b", 4)
G.add_edge("a", "c", 1)
G.add_edge("b", "e", 4)
G.add_edge("c", "b", 2)
G.add_edge("c", "d", 4)
G.add_edge("d", "e", 4)

dijkstra(G, "a")
