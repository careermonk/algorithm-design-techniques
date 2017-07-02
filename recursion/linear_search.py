def linear_search(A, i, j, k):
    if (i <=  j):
        if A[i] == k:
            return i
        else:
            return linear_search(A, i+1, j, k) 
    
    else:
        return -1

A = [3, -1, 5, 10, 9, 19, 14, 12, 8]
print linear_search(A, 0, len(A)-1, 12)
print linear_search(A, 0, len(A)-1, 6)
