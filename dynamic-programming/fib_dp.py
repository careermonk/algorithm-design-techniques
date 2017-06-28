# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def fib_dp(n):
    table = [None] * (n+1)
    for i in range(n+1):
        if i == 0 or i == 1:
            table[i] = i
        else:
            table[i] = table[i-1] + table[i-2]
    return table[n]

print(fib_dp(10))
