def find_depth_in_generic_tree(parent):
	max_depth = 0
	current_depth = 0
	for i in range (0, len(parent)):
		current_depth = 1
		j = i
		while(parent[j] != -1):
		       current_depth += 1
		       j = parent[j]
		if(current_depth > max_depth):
		       max_depth = current_depth
	
	return max_depth
	
parent=[-1, 0, 1, 6, 6, 0, 0, 2, 7]
print "Depth of given generic tree is:", find_depth_in_generic_tree(parent)
