def house_robber(A):
	n = len(A)
	M = [0] * (n+1)
	M[0] = A[0]
	M[1] = max(A[0], A[1])

	for i in range(2, n): 
		if( M[i-1] > M[i-2]  +A[i]):
			M[i] = M[i-1]
		else: 	
			M[i] = M[i-2] + A[i]	

	return M[n-1]

A = [-2, 3, -16, 100, -4, 5]
print house_robber(A)
