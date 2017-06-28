# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def house_robber(A):
	n = len(A)
	M = [0] * (n+1)
	M[0] = A[0]
	M[1] = max(A[0], A[1])

	for i in range(2, n):
		if( M[i-1] > M[i-2]  +A[i]):
			M[i] = M[i-1]
		else:
			M[i] = M[i-2] + A[i]

	return M[n-1]

A = [-2, 3, -16, 100, -4, 5]
print house_robber(A)
