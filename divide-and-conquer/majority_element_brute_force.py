def majority_element(A):
        for i in range(len(A)):
		counter = 0
		for j in range(len(A)):
			if (A[i] == A[j]):
				counter += 1
  
		if (counter > len(A)/2):
			return A[i]
	return None

A = [1, 2, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 7, 3, 3, 3]
print majority_element(A)
A = [3, 3, 5, 2, 5, 5, 2, 5, 5]
print majority_element(A)
A = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
print majority_element(A)
A = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print majority_element(A)
