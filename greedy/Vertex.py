#This class will implement a vertex for a Graph for the unweighted shortest path problem
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.parent = None
        self.distance = None

    def setParent(self, par):
        self.parent = par

    def getParent(self):
        return self.parent

    def setDist(self, d):
        self.distance = d

    def getDist(self):
        return self.distance

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " is connected to: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]
