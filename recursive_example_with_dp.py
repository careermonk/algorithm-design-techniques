def func_tabulation_dp(m, p):
    '''Using DP and using a dictionary as a table.'''
    table = {}
    for n in range(m+1):
        for r in range(min(n, p)+1):
            if r == 0 or n == r:
                table[n,r] = 1
            else:
                table[n,r] = table[n-1,r-1] + table[n-1,r]       
    return table[m,p]
      
print func_tabulation_dp(10, 5)
