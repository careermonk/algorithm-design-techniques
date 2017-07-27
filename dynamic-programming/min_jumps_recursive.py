def jumps(A, index):
	if (index >= len(A) - 1) :
		return 0
        
	minimum = float("infinity")
	i = 1
	while ( i <= A[index]):
		minimum = min(minimum, 1 + jumps(A, index + i))
		i = i +1
	return minimum

A = [2, 3, 1, 1, 4]
print jumps(A, 0)
A = [1, 4, 2, 1, 9, 3, 4, 5, 2, 7, 9]
print jumps(A, 0)
