# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.


# Returns 1 if A[] can be partitioned in two subsets of equal sum, otherwise 0
def find_partition(A):
	# calculate sum of all elements
	sum = 0
	n = len(A)
	for i in range(0,n):
		sum += A[i]
	# If sum is odd, there cannot be two subsets with equal sum
	if (sum%2 != 0):
		return False

	T = [[False for x in range(n+1)] for x in range(sum//2 + 1)]

	# initialize top row as true
	for i in range(0,n):
		T[0][i] = True

	# initialize leftmost column, except T[0][0], as 0
	for i in range(1,sum//2+1):
		T[i][0] = False

	# Fill the partition table in bottom up manner
	for i in range(1,sum//2+1):
		for j in range(0,n+1):
			T[i][j] = T[i][j-1]
			if (i >= A[j-1]):
				T[i][j] = T[i][j] or T[i - A[j-1]][j-1]
	return T[sum/2][n]
