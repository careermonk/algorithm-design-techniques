# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def max_contigous_sum_dp(A):
	maxSum = 0
	n = len(A)
	M = [0] * (n+1)
	M[0] = A[0]
	for i in range(1, n):
		M[i] = max(A[i], M[i-1] + A[i])

	for i in range(0, n):
		if(M[i]  > maxSum):
			maxSum = M[i]

	return maxSum

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print max_contigous_sum_dp(A)
