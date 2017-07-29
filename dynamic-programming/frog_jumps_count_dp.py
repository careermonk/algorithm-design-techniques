def frog_jumps(D, P):
	n = len(D)
	
	# Initialization
	table = [0 for i in range (P+1)]
	
	# Base case
	table[0] = 1

	for i in xrange(1, P + 1):
		for j in xrange(n):
			if D[j] <= i:
				table[i] = table[i] + table[i - D[j]]
	return table[P]

A = [2, 3, 1, 5, 4]
print frog_jumps(A, 15)
