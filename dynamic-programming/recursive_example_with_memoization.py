# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def func_memoization(m, p):
    '''Using memoization and using a dictionary as a table.'''
    table = {}
    def func(n, r):
        if (n, r) not in table:
            if r == 0 or n == r:
                table[n, r] = 1
            else:
                table[n, r] = func(n-1, r-1) + func(n-1, r)
        return table[n, r]
    return func(m, p)

print func_memoization(10, 5)
