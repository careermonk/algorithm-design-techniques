# Iterative Binary Search Algorithm
def binary_search(A, value):
    low = 0
    high = len(A)-1
    while low <= high: 
        mid = (low+high)//2
        if A[mid] > value: high = mid-1
        elif A[mid] < value: low = mid+1
        else: return mid
    return -1

def check_for_magic_index(A):
    X = [0 for i in range(len(A))]
    for i in range(len(A)):
		X[i] = A[i]-i

    return binary_search(X, 0)

A = [-1, 0, 2, 5, 7, 9, 11, 12, 19]
print check_for_magic_index(A)
