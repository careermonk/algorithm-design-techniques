class Graph:
    def __init__(self):
        self.vetextList = {}
        self.vetexCount = 0

    def addVertex(self, key):
        self.vetexCount += 1
        newVertex = Vertex(key)
        self.vetextList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vetextList:
            return self.vetextList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vetextList

    def addEdge(self, source, destination, cost=0):
        if source not in self.vetextList:
            nv = self.addVertex(source)
        if destination not in self.vetextList:
            nv = self.addVertex(destination)

        sourceVertex = self.vetextList[source]
        destinationVertex = self.vetextList[destination]

        sourceVertex.addNeighbor(destinationVertex, cost)

    def getVertices(self):
        return self.vetextList.keys()

    def __iter__(self):
        return (iter(self.vetextList.values()))
