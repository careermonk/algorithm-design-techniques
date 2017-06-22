def max_contigous_sum_brute_force_improvement(A):
	maxSum = 0
	n = len(A)
	for i in range(1, n): 
		currentSum = 0
		for j in range(i, n):	
			currentSum += A[j]
			if(currentSum > maxSum):
				maxSum = currentSum
	return maxSum


A = [1, -3, 4, -2, -1, 6]
print max_contigous_sum_brute_force_improvement(A)
