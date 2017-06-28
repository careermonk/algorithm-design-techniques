def majority_element(A):
	A.sort()
	return A[len(A)/2]

A = [1, 2, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 7, 3, 3, 3]
print majority_element(A)
