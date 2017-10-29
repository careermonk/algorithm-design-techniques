# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def get_OBST(A, F, i, j, level):
    if i > j:
        return 0
    min_value = float("inf")

    for index in range(i, j + 1):
        val = (get_OBST(A, F, i, index - 1, level + 1)   # left tree
               + level * F[index]                                    # value at level
               + get_OBST(A, F, index + 1, j, level + 1)) # right tree
        min_value = min(val, min_value)

    return min_value

def OBST(A, F):
    return get_OBST(A, F, 0, len(A) - 1, 1)

A = [10, 12, 20, 35, 46]
F = [34, 8, 50, 21, 16]
print OBST(A, F)
