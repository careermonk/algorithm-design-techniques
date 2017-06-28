# Iterative Binary Search Algorithm
def check_for_magic_index(A):
	low = 0
	high = len(A)-1
	while low <= high: 
		mid = (low+high)//2
		if mid == A[mid]: 	# check for magic index.
			return mid
		elif A[mid] > mid: 
			high = mid-1
		else: 				# A[mid] < mid: 
			low = mid+1
	return -1

A = [-1, 0, 2, 5, 7, 9, 11, 12, 19]
print check_for_magic_index(A)
