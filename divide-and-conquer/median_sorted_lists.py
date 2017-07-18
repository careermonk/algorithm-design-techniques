
def median(A, B):
	m = len(A) + len(B)

	if m % 2 == 1:
		return kth(A, B, m // 2)
	else:
		return float(kth(A, B, m // 2) + kth(A, B, m // 2 - 1)) / 2
    
def kth(A, B, k):
	if not A:
		return B[k]
	if not B:
		return A[k]

	midA, midB = len(A) // 2, len(B) // 2

	if midA + midB < k:
		if A[midA] > B[midB]:
			return kth(A, B[midB + 1:], k - midB - 1)
		else:
			return kth(A[midA + 1:], B, k - midA - 1)
	else:
		if A[midA] > B[midB]:
			return kth(A[:midA], B, k)
		else:
			return kth(A, B[:midB], k)

A = [1, 2, 3, 4, 5, 6, 7]
B = [2, 3, 4, 5, 6, 8, 9]
print median(A, B)
		
A = [1, 2, 4, 7, 9]
B = [3, 5, 6, 8]
print median(A, B)
