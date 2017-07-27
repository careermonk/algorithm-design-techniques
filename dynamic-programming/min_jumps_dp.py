def jumps(A):
	n = len(A)
	table = [float("infinity") for i in range (n)]
	table[0] = 0
	for i in range(n-1):
		for j in range(1, A[i]+1):
			if (i + j < n):
				table[i+j] = min(table[i+j], 1 + table[i])
	return table[n-1]

A = [2, 3, 1, 1, 4]
print jumps(A)

A = [1, 4, 2, 1, 9, 3, 4, 5, 2, 7, 9]
print jumps(A)
