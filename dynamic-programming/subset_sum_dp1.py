# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def subset_sum(A):
	n = len(A)
	K = 0
	for i in range(0, n): 
		K += A[i]
	T = [0] * (K+1)
	T[0] = 1
	for i in range(1, K+1): 	
		T[i] = 0
	# process the numbers one by one
	for i in range(0, n): 
		for j in range(K - A[i], 0, -1): 
			if( T[j] ): 
				T[j + A[i]] = 1
	return T[K//2]

A = [3,2,4,19,3,7,13,10,6,11]
print subset_sum(A)
