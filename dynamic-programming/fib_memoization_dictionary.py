# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

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
