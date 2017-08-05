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
def k_smallest(A, k):
	"Find k smallest elements"
	A = list(A)
	result = []
	if not 0 <= k < len(A):
		raise ValueError('not enough elements')

	while True:
		pivot = random.randrange(len(A))
		pivotCount = 0
		under, over = [], []
		for elem in A:
			if elem < A[pivot]:
				under.append(elem)
			elif elem > A[pivot]:
				over.append(elem)
			else:
				pivotCount += 1
		if k < len(under):
			A = under
		elif k < len(under) + pivotCount:
			result.extend(under)
			result.extend([A[pivot] for i in range(pivotCount)])
			return result
		else:
			result.extend(under)
			result.extend([A[pivot] for i in range(pivotCount)])
			A = over
			k = k - len(under) - pivotCount
	return result

A= [2,1,5,234,3,44,7,6,4,9,11,12,14,13]
for i in range (len(A)):
    print k_smallest(A, i)
