def maxmin(A):
	n = len(A)
	if (n == 1):
		return A[1], A[1]
	elif (n == 2):
		if( A[0] < A[1]):
			return A[0], A[1]
		else:
			return A[1], A[0]
	else:
		min_left, max_left = maxmin(A[:n/2])
		min_right, max_right = maxmin(A[n/2:])

		if (min_left < min_right):
			minimum = min_left
		else:
			minimum = min_right

		if (max_left < max_right):
			maximum = max_right
		else:
			maximum = max_left

		return (minimum, maximum)
	
print maxmin([3, 42, 29, 1, 45, 9, 69, 19])
