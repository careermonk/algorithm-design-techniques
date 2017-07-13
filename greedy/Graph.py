from Vertex import *
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
