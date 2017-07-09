def edit_distance(A, B):
    m=len(A)+1
    n=len(B)+1
    
    table = {}
    for i in range(m): 
        table[i,0]=i
    for j in range(n): 
        table[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if A[i-1] == B[j-1] else 1
            table[i,j] = min(table[i, j-1]+1, table[i-1, j]+1, table[i-1, j-1]+cost)

    return table[i,j]
print edit_distance("Ceil", "trials")
print edit_distance("pea", "ate")
print(edit_distance("Helloworld", "HalloWorld"))
