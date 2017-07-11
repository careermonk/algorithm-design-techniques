def topological_sort(graph):
    topologicalSortedList = []  		#result
    zeroInDegreeVertexList = [] 		#node with 0 in-degree/inbound neighbours
    inDegree = { u : 0 for u in graph } 	#inDegree/inbound neighbours

    #Step 1: Iterate graph and build in-degree for each vertex
    #Time complexity: O(V+E) - outer loop goes V times and inner loop goes E times
    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    #Step 2: Find vertex(s) with 0 in-degree
    for k in inDegree:
        #print(k,inDegree[k])
        if (inDegree[k] == 0):
            zeroInDegreeVertexList.append(k)           

    #Step 3: Process nodes with in-degree = 0
    while zeroInDegreeVertexList:
        v = zeroInDegreeVertexList.pop(0) #order in important!
        topologicalSortedList.append(v)
        #Step 4: Update in-degree
        for neighbour in graph[v]:
            inDegree[neighbour] -= 1
            if (inDegree[neighbour] == 0):
                zeroInDegreeVertexList.append(neighbour)

    return topologicalSortedList
    

#Adjacency list
graph = {
        'Foundations': set(['Walls works']),
        'Walls works': set(['Plumbing works', 'Windows works', 'Roof works']),
	'Plumbing works': set(['Interior decorations']),
	'Windows works': set(['Interior decorations']),
	'Roof works': set(['Interior decorations']),
	'Interior decorations': set([])
        }

result = topological_sort(graph)
print("Topological sort >>> ", result)
# check if #nodes in result == #nodes in graph
if (len(result) == len(graph)):
    print("Given graph is a Directed Acyclic Graph!")
else:
    print("Given graph has cycles and not possible to find topological order!")
