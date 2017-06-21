def lucky_tabulation_dp(n):
    '''Using DP and using a dictionary as a table.'''
    table = {}
    for i in range(n+1):
      if i == 0:
          table[i] = 0
      elif i == 1:
          table[i] = 1
      else:
          table[i] = 10*table[i-1] - table[i-2]       
    return table[n]
      
print lucky_tabulation_dp(3)
