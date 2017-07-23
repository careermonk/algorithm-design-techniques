def shuffle(A):
	n = len(A)//2
	i =0; q =1; k = n
	while (i<n):
		j = k
		while j > i+ q:
			A[j], A[j-1] = A[j-1], A[j]
			j -= 1
		i += 1; k += 1; q += 1
A = [11, 12, 13, 14, 15, 16, 17, 18]
shuffle(A)
print A
