def lis(A):
    LIS = [1 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(i):
            if A[j] <= A[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
    return max(LIS)
    
A = [5, 8, 9, 20, 14, 2, 7, 19]
print lis(A)
