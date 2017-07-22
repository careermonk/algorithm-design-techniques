def max_max(A):
	if not A:
		return None, None
	# if A contains only 1 item return -1 (a dummy item) and that item
	if len(A) == 1:          
		return (-1, A[0])      
	elif len(A) == 2:
		if A[0] <= A[1]: 
			return (A[0], A[1]) 
		else:
			return (A[1], A[0])
	else:  # general case
		if A[0] <= A[1]: 
			max1, max2 = A[0], A[1] 
		else:
			max1, max2 = A[1], A[0]

		for i in range(2, len(A)):
			if A[i] >= max2:                 		
				max1 = max2
				max2 = A[i]  
			elif: A[i] >= max1
				max1 = A[i] 
    
	return (max1, max2)  # return the overall maximal items

A = [3, 4, 29, 41, 45, 49, 79, 89]
print max_max(A)
