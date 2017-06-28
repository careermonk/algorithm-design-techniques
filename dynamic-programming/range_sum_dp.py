# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

cumulative_sum = []
def cumulative_sum_pre_process(A):
	global cumulative_sum
	cumulative_sum.append(A[0])
	for i in range(0, len(A)):
		cumulative_sum.append(cumulative_sum[i] + A[i])

def range_sum_dp(A, start_index, end_index):
    return cumulative_sum[end_index+1] - cumulative_sum[start_index]

A= [-2, 1, 6, -5, 9, -1, 19]
cumulative_sum_pre_process(A)
print range_sum_dp(A, 0, 3)
print range_sum_dp(A, 2, 6)
print range_sum_dp(A, 5, 5)
