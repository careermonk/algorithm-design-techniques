# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def max_contigous_sum_brute_force(A):
	maxSum = 0
	n = len(A)
	for i in range(1, n):
		for j in range(i, n):
			currentSum = 0
			for k in range(i, j+1):
				currentSum += A[k]
				if(currentSum > maxSum):
					maxSum = currentSum
	return maxSum

A = [1, -3, 4, -2, -1, 6]
print max_contigous_sum_brute_force(A)
