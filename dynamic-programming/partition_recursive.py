# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

# A utility function that returns True if there is a subset of A[] with sum equal to given sum
def subset_sum (A, n, sum):
	if (sum == 0): 
		return True
	if (n == 0 and sum != 0):
		return False
	# If last element is greater than sum, then ignore it
	if (A[n-1] > sum):
		return subset_sum(A, n-1, sum)

	return subset_sum(A, n-1, sum) or subset_sum(A, n-1, sum-A[n-1])

# Returns True if A[] can be partitioned in two subsets of equal sum, otherwise False
def find_partition(A):
	# calculate sum of all elements
	sum = 0
	n = len(A)
	for i in range(0,n):
		sum += A[i]

	# If sum is odd, there cannot be two subsets with equal sum
	if (sum%2 != 0):
		return False

	# Find if there is subset with sum equal to half of total sum
	return subset_sum(A, n, sum/2)
