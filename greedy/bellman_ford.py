from Vertex import *
from Graph import *
from PriorityQueue import *

def bellman_ford(G, s):
    
    #set distance for all other vertices to "infinity"
    inf = float("infinity")
    for i in G.get_vertices():
        v = G.get_vertex(i)
        v.set_distance(inf)
    
    #set distance of source to zero
    source = G.get_vertex(s)
    source.set_distance(0)

    for i in G.get_vertices():
        for (fr, to, cost) in G.get_edges():   
            #print fr, to, cost
            u = G.get_vertex(fr)
            v = G.get_vertex(to)
            if v.get_distance() > (u.get_distance() + u.get_weight(v)):
                v.set_previous(u)
                v.set_distance(u.get_distance() + u.get_weight(v))

    #loop over all nodes and print their distances
    for i in G.get_vertices():
        u = G.get_vertex(i)
        print "Node", u.get_vertex_ID(), "with distance", u.get_distance()

# Test Code
#create an empty graph
G = Graph()
    
#add vertices to the graph
for i in ["a", "b", "c", "d", "e"]:
    G.add_vertex(i)

#add edges to the graph - need one for each edge to make them undirected
#since the edges are unweighted, make all cost 1
G.add_edge("a", "c", 6)
G.add_edge("a", "d", 3)
G.add_edge("b", "a", 3)
G.add_edge("c", "d", 2)
G.add_edge("d", "c", 1)
G.add_edge("d", "b", 1)
G.add_edge("e", "b", 4)
G.add_edge("e", "d", 2)

bellman_ford(G, "a")
