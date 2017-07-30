def lis(A, d):
	LIS = [1 for _ in range(len(A))]
	for i in range(len(A)):
		for j in range(i):
			if A[j] + d <= A[i]:
				LIS[i] = max(LIS[i], LIS[j] + 1)

	## trace subsequence back to output
	result = []
	element = LIS[len(LIS)-1]
	for i in  range(len(LIS)-1, -1, -1):
		if LIS[i] == element:
			result.append(A[i])
			element -=  1

	return list(result.__reversed__())
    
A = [5, 8, 9, 20, 14, 2, 7, 19]
print lis(A, 2)
