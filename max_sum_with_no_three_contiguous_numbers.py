def max_sum_with_no_three_contiguous_numbers(A):
	n = len(A)
	M = [0] * (n)
	M[0] = A[0]
	M[1] = max(A[0], A[1], A[0] + A[1])
	M[2] = max(M[1], A[2] + M[0], A[2] + A[1])

	for i in range(3, n): 
		M[i] = max(M[i-1], A[i] + M[i-2], A[i] + A[i-1] + M[i-3])

	print M
	return M[n-1]

A = [2, 13, 16, 100, 4, 5]
print max_sum_with_no_three_contiguous_numbers(A)
