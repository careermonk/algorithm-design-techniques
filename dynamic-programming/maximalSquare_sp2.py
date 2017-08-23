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

	L = [0] * (len(matrix[0])+1)
	maxsqlen = 0
	previous = 0
	for i in xrange(0, len(matrix)):
		for j in xrange(0, len(matrix[0])):
			temp = L[j]
			if matrix[i][j] == 1:
				if i == 0 or j == 0:
					L[j] = 1
				else:
					L[j] = min(L[j-1], L[j], previous) + 1
			
				maxsqlen = max(maxsqlen, L[j])
			else:
			    L[j] = 0
			previous = temp
	return maxsqlen

matrix=[	[0,  1,  1,  0,  1], 
		[1,  1,  0,  1,  0], 
		[0,  1,  1,  1,  0], 
		[1,  1,  1,  1,  0], 
		[1,  1,  1,  1,  1], 
		[0,  0,  0,  0,  1]]

print maximalSquare(matrix)
