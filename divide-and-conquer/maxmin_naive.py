def maxmin(A):
	if not A:
		return None, None
	minimum = A[0]
	maximum = A[0]
	for i in range(1, len(A)):
		if A[i] < minimum:  
			minimum = A[i] 
		if A[i] > maximum:  
			maximum = A[i] 
	
	return minimum, maximum

print maxmin([3, 42, 29, 1, 45, 9, 69, 19])
