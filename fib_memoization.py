def fib_memoization(m):
    table = (m + 1) * [None]
    def func(n):
        if table[n] == None:
            if n <= 1:
                table[n] = n
            else:
                table[n] = func(n-1) + func(n-2)
        return table[n]
    return f(m)
      
print(fib_memoization(10))
