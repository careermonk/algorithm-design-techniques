def lucky(n):
    '''lucky implementation with recursion'''
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return 10*lucky(n-1) - lucky(n-2)
      
print lucky(3)
