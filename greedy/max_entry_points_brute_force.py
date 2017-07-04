def max_entry_points(edges):
    n = len(edges)
    count = max = 0
    for i in range(0,n):
        count  = 1
        for j in range(0,n):
            if( i != j and edges[i] == edges[j]):
                count += 1
        if max< count:
            max = count
            max_entry_point_cell = edges[i]
    print "Cell", max_entry_point_cell, "has", max, "entrypoints."

edges = [4, 4, 1, 4, 13, 8, 8, 8, 0, -1, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, -1, 21]
max_entry_points(edges)
