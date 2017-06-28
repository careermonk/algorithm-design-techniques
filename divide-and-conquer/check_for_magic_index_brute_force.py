def check_for_magic_index(A):
	for i in range(len(A)):
		if(A[i] == i) :
			return i
	return None

A = [-1, 0, 2, 5, 7, 9, 11, 12, 19]
print check_for_magic_index(A)
