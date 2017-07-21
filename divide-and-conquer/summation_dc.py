def summation(A, start, end):
	if (start == end):
		return A[start]
	else:
		if start == end-1:
			return A[start] + A[end]
		else:
			mid = start + (end-start)/2
			left_sum = summation(A, start, mid)
			right_sum = summation(A, mid+1, end)
			return left_sum + right_sum

A = [3, 4, 2, 1, 5, 8, 7, 6]
		
print summation(A, 0, len(A)-1)
