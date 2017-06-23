def range_sum(A, start_index, end_index):
    sum = 0
    for i in range(start_index, end_index+1):
        sum += A[i]

    return sum

A= [-2, 1, 6, -5, 9, -1, 19]
print range_sum(A, 0, 3)
print range_sum(A, 2, 6)
print range_sum(A, 5, 5)
