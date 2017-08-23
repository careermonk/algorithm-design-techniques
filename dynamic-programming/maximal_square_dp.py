# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def maximalSquare(matrix):
	if len(matrix) == 0:
	    return 0
	L = [[0]*len(matrix[0]) for i in xrange(0, len(matrix))]
	maxsqlen = 0
	for i in xrange(0, len(matrix)):
		for j in xrange(0, len(matrix[0])):
			if matrix[i][j] is 1:
				if i == 0:
					L[i][j] = 1
				elif j == 0:
					L[i][j] = 1
				else:
					L[i][j] = min(L[i - 1][j], L[i][j - 1], L[i - 1][j - 1]) + 1
				maxsqlen = max(maxsqlen, L[i][j])
	return maxsqlen

matrix=[	[0,  1,  1,  0,  1], 
		[1,  1,  0,  1,  0], 
		[0,  1,  1,  1,  0], 
		[1,  1,  1,  1,  0], 
		[1,  1,  1,  1,  1], 
		[0,  0,  0,  0,  1]]

print maximalSquare(matrix)
