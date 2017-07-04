def max_entry_points(edges):
	edges.sort()
	count = max = 1
	element = edges[0]
	
	# Skipping -1 as they were not really the cells
	for i in range(1,len(edges)):
	    if (edges[i] != -1):
	        break
	
	for i in range(i,len(edges)):
		if (edges[i] == element):
			count += 1
			if count > max:
				max =  count
				max_entry_point_cell = element
		else:
			count = 1
			element = edges[i]
	print "Cell", max_entry_point_cell, "has", max, "entrypoints."

edges = [4, 4, 1, 4, 13, 8, 8, 8, 0, -1, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, -1, 21]
max_entry_points(edges)
