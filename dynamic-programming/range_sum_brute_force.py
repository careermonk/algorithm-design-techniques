# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def range_sum(A, start_index, end_index):
    sum = 0
    for i in range(start_index, end_index+1):
        sum += A[i]

    return sum

A= [-2, 1, 6, -5, 9, -1, 19]
print range_sum(A, 0, 3)
print range_sum(A, 2, 6)
print range_sum(A, 5, 5)
