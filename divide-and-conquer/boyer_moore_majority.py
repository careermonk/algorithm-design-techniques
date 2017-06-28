def majority_element(A):
	count = 0
	element = -1
	n = len(A)
	if n == 0:
		return
	for i in range(0, n-1):
		if(count == 0) :
			element = A[i]
			count = 1
		elif(element == A[i]):
			count += 1
		else:
			count -= 1
	return element

A = [1, 2, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 7, 3, 3, 3]
print majority_element(A)
A = [3, 3, 5, 2, 5, 5, 2, 5, 5]
print majority_element(A)
A = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
print majority_element(A)
A = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print majority_element(A)
