# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def count_fence_painting_ways(n, k):
	temp = 0
	previous_one = k
	previous_two = k*k
	if n == 0: return temp
	if n == 1: return previous_one
	if n == 2: return previous_two
	for i in range(3, n):
		current = (k - 1) * (previous_two + previous_one)
		previous_one = previous_two
		previous_two = current

	return current

print count_fence_painting_ways(5,4)
