def fib_memoization_dictionary(n):
    '''Using memoization and using a dictionary as a table.'''
    table = {}
    def func(m):
        if m not in table:
            if m <= 1:
                table[m] = m
            else:
                table[m] = func(m-1) + func(m-2)
        return table[m]
    return func(n)
      
print(fib_memoization_dictionary(10))
