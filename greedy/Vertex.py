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
