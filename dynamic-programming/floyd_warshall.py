# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def adj(graph):
    vertices = graph.keys()
 
    D = {}
    for i in vertices:
        D[i] = {}
        for j in vertices:
            try:
                D[i][j] = graph[i][j]
            except KeyError:
                # the distance from a node to itself is 0
                if i == j:
                    D[i][j] = 0
                    # the distance from a node to an unconnected node is infinity
                else:
                    D[i][j] = float('inf')
    return D

def floyd_warshall(graph):
    vertices = graph.keys()
 
    d = dict(graph) # copy graph
    for k in vertices:
        for i in vertices:
            for j in vertices:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
 

if __name__ == "__main__":
    graph = {'c': {'a':5, 'b':2, 'd':1, 'h':2},
                'a': {'b':3, 'c':5, 'e':8, 'f':1},
                'b': {'a':3, 'c':2, 'g':1},            
                'd': {'c':1, 'e':4},
                'e': {'a':8, 'd':4, 'f':6, 'h':1},
                'f': {'a':1, 'e':6, 'g':5},
                'g': {'b':1, 'f':5, 'h':1},
                'h': {'c':2, 'e':1, 'g':1}}
    matrix=adj(graph)
    print     matrix
    print floyd_warshall(matrix)
    
