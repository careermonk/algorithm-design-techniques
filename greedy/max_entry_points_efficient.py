def max_entry_points(edges):
	n = len(edges)
	max = 0
	for i in range(0,len(edges)):
		if edges[i] == -1:
			continue
		edges[edges[i]%n] += n
	for i in range(0,len(edges)):
		 if(edges[i]/n > max): 
			max = edges[i]/n
			max_entry_point_cell =i
	print "Cell", max_entry_point_cell, "has", max-1, "entrypoints."

edges = [4, 4, 1, 4, 13, 8, 8, 8, 0, -1, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, -1, 21]
max_entry_points(edges)
