def majority_element(A):
	count = 0
	element = -1
	n = len(A)
	if n == 0:
		return
	for i in range(n):
		if(count == 0) :
			element = A[i]
			count = 1
		elif(element == A[i]):
			count += 1
		else:
			count -= 1

	# check if elements appears for more than n/2 times
	count = 0
	for i in range(n):
		if(element == A[i]):
			count += 1
	
	if count > len(A)/2:
		return element

	return None

A = [1, 2, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 7, 3, 3, 3]
print majority_element(A)
