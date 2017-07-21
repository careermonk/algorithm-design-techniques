def kthSmallest(A, B, k):
	while k > 0:
		m = len(A)
		n = len(B)

		if k >= m + n:
			return -1

		if(k == 1):
			return min(A[0], B[0])

		if(m == 0 and n > 0):
			return B[k-1]

		if(n == 0 and m > 0):
			return A[k-1] 

		i =  min(m-1, k/2) 
		j =  min(n-1, k/2) 
		
		if (B[j - 1] <= A[i] < B[j ]):
		    return A[i]
		 
		if (A[i - 1] <= B[j] < A[i]):
			    return B[j]
			    
		if(A[i] < B[j]):
		    A = A[i:]
		    B = B[:j+1]
		else:
		    A = A[:i+1]
		    B = B[j:]
        k = k - i

	return -1
	
A = [1, 5, 8, 10, 50]
B = [3, 4, 29, 41, 45, 49, 79, 89]
print kthSmallest(A, B, 10)
