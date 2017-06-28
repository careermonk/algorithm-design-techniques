# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def count_fence_painting_ways(n, k):
    table = [0 for j in range(n)]
    table[0] = 0
    table[1] = k
    table[2] = k*k

    for i in range(3, n):
        table[i] = (k - 1) * (table[i-1] + table[i-2])
        table[i-2] = table[i-1]
        table[i-1] = table[i]

    return table[n-1]

print count_fence_painting_ways(5,4)
