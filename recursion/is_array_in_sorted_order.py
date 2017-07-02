def is_sorted(A):
	# Base case
	if len(A) == 1:
	    return True
	else:
	    return A[0] <= A[1] and is_sorted(A[1:])

A = [127, 220, 246, 277, 321, 454, 534, 565, 933]	
print(is_sorted(A))    
