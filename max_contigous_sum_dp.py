def max_contigous_sum_dp(A):
	maxSum = 0
	n = len(A)
	M = [0] * (n+1)
	M[0] = A[0]
	for i in range(1, n): 
		M[i] = max(A[i], M[i-1] + A[i])

	for i in range(0, n): 
		if(M[i]  > maxSum):
			maxSum = M[i]

	return maxSum
	
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print max_contigous_sum_dp(A)
