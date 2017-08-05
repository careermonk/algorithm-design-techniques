# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def kth_smallest( A, k ):
	if k >= len(A):
		return None
	for i in range( k ):
		smallest = i
		for j in range( i + 1 , len(A) ):
			if A[j] < A[smallest]:
				smallest = j
	
		A[smallest], A[i] = A[i], A[smallest]
	return A[k-1]

A = [10, 5, 1, 6, 20, 19, 22, 29, 32, 9]
print kth_smallest(A, 3)
