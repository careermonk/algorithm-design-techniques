def catalan_recursive(n):
  if n == 0:
    return 1
  else:
    count = 0
    for i in range(n):
      count += catalan_recursive(i) * catalan_recursive(n - 1 - i)
  return count	

print catalan_recursive(3)
