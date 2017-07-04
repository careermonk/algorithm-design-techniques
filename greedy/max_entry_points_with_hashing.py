def max_entry_points(edges):
	table = {} 	# hash
	max = 0
	for element in edges:
	    if element in table:
			table[element] += 1
	    elif element != " ":
			table[element] = 1
	    else:
			table[element] = 0
	for element in edges:
	    if table[element] > max:
			max = table[element]
			max_entry_point_cell = element
	print "Cell", max_entry_point_cell, "has", max, "entrypoints."

edges = [4, 4, 1, 4, 13, 8, 8, 8, 0, -1, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, -1, 21]
max_entry_points(edges)
