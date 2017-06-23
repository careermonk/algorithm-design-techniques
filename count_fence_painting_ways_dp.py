def count_fence_painting_ways(n, k):
    table = [0 for j in range(n)]
    table[0] = 0
    table[1] = k
    table[2] = k*k

    for i in range(3, n):
        table[i] = (k - 1) * (table[i-1] + table[i-2])
        table[i-2] = table[i-1]
        table[i-1] = table[i]
    
    return table[n-1]

print count_fence_painting_ways(5,4)
