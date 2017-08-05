# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

import random
def kth_smallest(A, k):
    "Find the nth rank ordered element (the least value has rank 0)."
    if not 0 <= k < len(A):
        raise ValueError('not enough elements for the given rank')

    while True:
        pivotIndex = random.randrange(len(A))
        pivotCount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in A:
            if elem < A[pivotIndex]:
                uappend(elem)
            elif elem > A[pivotIndex]:
                oappend(elem)
            else:
                pivotCount += 1
        if k < len(under):
            A = under
        elif k < len(under) + pivotCount:
            return A[pivotIndex]
        else:
            A = over
            k -= len(under) + pivotCount
	
A= [2,1,5,234,3,44,7,6,4,9,11,12,14,13]
for i in range (len(A)):
    print kth_smallest(A, i)
