def jumps(A, index, P):
	if (index >= P) :
		return 0

	minimum = float("infinity")
	i = 0
	while ( i < len(A)):
		if index + A[i] <= P:
			minimum = min(minimum, 1 + jumps(A, index + A[i], P))
		i = i + 1
	return minimum

A = [1, 4, 5, 2]
print jumps(A, 0, 18)
