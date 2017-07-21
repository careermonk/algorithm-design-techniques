def kthSmallest(A, B, k):
    m = len(A); n= len(B)
    if k >= m + n:
        return -1
    if m == 0:
        return B[k]
    elif n == 0:
        return A[k]

    i = m/2
    j = n/2
    if i+j<k:
        if A[i]>B[j]:
            return kthSmallest(A, B[j+1:], k-j-1)
        else:
            return kthSmallest(A[i+1:], B, k-i-1)
    else:
        if A[i]>B[j]:
            return kthSmallest(A[:i], B, k)
        else:
            return kthSmallest(A, B[:j], k)
	
A = [3, 4, 29, 41, 45, 49, 79, 89]
B = [1, 5, 8, 10, 50]
for i in range(14):
    print kthSmallest(A, B, i)
