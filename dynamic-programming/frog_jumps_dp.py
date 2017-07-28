def jumps(A, P):
	n = len(A)
	table = [float("infinity") for i in range (P)]
	table[0] = 0
	for i in range(0, P):
		for j in range(n):
			if (i + A[j] < P):
				table[i+A[j]] = min(table[i+A[j]], 1 + table[i])
	return table[P-1]

A = [1, 4, 5, 2]
print jumps(A, 18)
