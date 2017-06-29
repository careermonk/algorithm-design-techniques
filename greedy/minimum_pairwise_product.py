def minimum_pairwise_product(A):
	# Sort A in ascending order
	A.sort()
	min_product = 0
	j = len(A)-1
	for i in range( len(A)//2 ):
		min_product += A[i]*A[j]
		j -= 1
        return min_product

A = [6, 2, 9, 4, 5, 1, 6, 7]
print minimum_pairwise_product(A)
