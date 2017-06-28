# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

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
