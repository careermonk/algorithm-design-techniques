def max_contigous_sum_brute_force(A):
	maxSum = 0
	n = len(A)
	for i in range(1, n): 	
		for j in range(i, n):	
			currentSum = 0
			for k in range(i, j+1):	
				currentSum += A[k]
				if(currentSum > maxSum):
					maxSum = currentSum
	return maxSum

A = [1, -3, 4, -2, -1, 6]
print max_contigous_sum_brute_force(A)
