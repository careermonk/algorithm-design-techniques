def summation(A):
	s = 0
	for i in range(len(A)):
		s = s+ A[i]
	return s

A = [3, 4, 2, 1, 5, 8, 7, 6]		
print summation(A)
