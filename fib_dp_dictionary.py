def fib_dp_dictionary(n):
    '''using dynamic programming and using dictionary as a table.'''
    table = {}
    for i in range(n+1):
        if i == 0 or i == 1:
            table[i] = i
        else:
            table[i] = table[i-1] + table[i-2]
    return table[n]
      
print(fib_dp_dictionary(10))
