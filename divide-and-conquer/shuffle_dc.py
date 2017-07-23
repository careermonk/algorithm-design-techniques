def shuffle(A, start, end):
	#Array center
	mid = start + (end-start)/2
	left_mid = 1 + start + (mid-start)//2

	if(start == end): # Base case when the array has only one element
		return
	k = 1
	i = left_mid
	while(i<=mid):	
		# Swap elements around the center
		A[i], A[mid + k] = A[mid + k], A[i]	
		i += 1
		k += 1
	
	shuffle (A, start, mid)	# Recursively call the function on the left and right
	shuffle (A, mid + 1, end)	# Recursively call the function on the right

A = [11, 12, 13, 14, 15, 16, 17, 18]
shuffle(A, 0, len(A)-1)
print A
