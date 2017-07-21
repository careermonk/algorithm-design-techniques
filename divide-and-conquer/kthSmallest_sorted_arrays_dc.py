def kthSmAllest(A, B, k):
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
            return kthSmAllest(A, B[j+1:], k-j-1)
        else:
            return kthSmAllest(A[i+1:], B, k-i-1)
    else:
        if A[i]>B[j]:
            return kthSmAllest(A[:i], B, k)
        else:
            return kthSmAllest(A, B[:j], k)
	
A = [3, 4, 29, 41, 45, 49, 79, 89]
B = [1, 5, 8, 10, 50]
print kthSmAllest(A, B, 1)
print kthSmAllest(A, B, 2)
print kthSmAllest(A, B, 3)
print kthSmAllest(A, B, 4)
print kthSmAllest(A, B, 5)
print kthSmAllest(A, B, 6)
print kthSmAllest(A, B, 7)
print kthSmAllest(A, B, 8)
print kthSmAllest(A, B, 9)
print kthSmAllest(A, B, 10)
print kthSmAllest(A, B, 11)
print kthSmAllest(A, B, 12)
print kthSmAllest(A, B, 13)
