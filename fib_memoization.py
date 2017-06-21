def fib_memoization(n):
    table = (n + 1) * [None]
    def func(m):
        if table[m] == None:
            if m <= 1:
                table[m] = m
            else:
                table[m] = func(m-1) + func(m-2)
        return table[m]
    return func(n)
      
print(fib_memoization(10))
