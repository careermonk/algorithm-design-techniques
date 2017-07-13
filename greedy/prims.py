from Vertex import *
from Graph import *
from PriorityQueue import *

def prim(G,start):
    pq = PriorityQueue()
    inf = float("infinity")
    for i in G.get_vertices():
        v = G.get_vertex(i)
        v.set_distance(inf)
        v.set_previous(None)

    s = G.get_vertex(start)
    s.set_distance(0)
    for v in G:
        pq.add(v.get_distance(), v.get_vertex_ID())
        
    MST = []
    
    while not pq.empty():
        t = pq.extract_min()
        currentVert = G.get_vertex(t[1])
        MST.append((currentVert.get_previous(), currentVert.get_vertex_ID()))
        for nextVert in currentVert.get_connections():
          newCost = currentVert.get_weight(nextVert) + currentVert.get_distance()
          if nextVert in pq and newCost<nextVert.get_distance():
              nextVert.set_previous(currentVert)
              nextVert.set_distance(newCost)
              pq.replace_key(nextVert,newCost)

    print MST

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

prim(G, "a")
