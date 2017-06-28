# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def max_sum_with_no_three_contiguous_numbers(A):
	n = len(A)
	M = [0] * (n)
	M[0] = A[0]
	M[1] = max(A[0], A[1], A[0] + A[1])
	M[2] = max(M[1], A[2] + M[0], A[2] + A[1])

	for i in range(3, n):
		M[i] = max(M[i-1], A[i] + M[i-2], A[i] + A[i-1] + M[i-3])

	print M
	return M[n-1]

A = [2, 13, 16, 100, 4, 5]
print max_sum_with_no_three_contiguous_numbers(A)
