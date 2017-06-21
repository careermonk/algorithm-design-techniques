def func(n, r):
    if r == 0 or r >= n: 
      return 1
    else:                 
      return func(n - 1, r - 1) + func(n - 1, r)

print func(10, 5)
