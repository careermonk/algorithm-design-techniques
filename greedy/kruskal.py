parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        fr, to, weight = edge
        if find(fr) != find(to):
            union(fr, to)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'edges': set([
            ('A', 'C', 7), ('A', 'D', 5),	
            ('B', 'C', 8), ('B', 'E', 5),	
            ('C', 'D', 9), ('C', 'E', 7),	
            ('D', 'E', 15), ('D', 'F', 6),
            ('E', 'F', 8), ('E', 'G', 9),
            ('F', 'G', 11), 	
            ])
        }

minimum_spanning_tree = set([('A', 'D', 5), ('A', 'C', 7), ('D', 'F', 6), ('E', 'G', 9), ('B', 'C', 8), ('B', 'E', 5),])
assert kruskal(graph) == minimum_spanning_tree
