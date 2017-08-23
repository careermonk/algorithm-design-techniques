# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

maxsqlen = 0
def maximalSquare(matrix, m, n):
	global maxsqlen
	# base condition: single row or single column
	if (m == 0 or n == 0):
		return matrix[m][n]

	# base condition
	if (matrix[m][n] == 0):
		return matrix[m][n]

	# find largest square matrix ending at matrix[m][n-1]
	left = maximalSquare(matrix, m, n - 1)

	# find largest square matrix ending at matrix[m-1][n]
	top = maximalSquare(matrix, m - 1, n)
	
	# find largest square matrix ending at matrix[m-1][n-1]
	diagonal = maximalSquare(matrix, m - 1, n - 1)
	
	# minimum of top, left, and diagonal
	size = 1 + min (min(top, left), diagonal)

	# update maximum size found so far
	maxsqlen = max(maxsqlen, size)

	# return the size of largest square matrix ending at matrix[m][n]
	return size

matrix=[	[0,  1,  1,  0,  1], 
		[1,  1,  0,  1,  0], 
		[0,  1,  1,  1,  0], 
		[1,  1,  1,  1,  0], 
		[1,  1,  1,  1,  1], 
		[0,  0,  0,  0,  1]]
rows = len(matrix)
columns = len(matrix[0])
maximalSquare(matrix, rows-1, columns-1)
print maxsqlen
