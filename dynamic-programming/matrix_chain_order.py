# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def matrix_chain_order(P):
	"""
	Input: P[] = {40, 20, 30, 10, 30}   
	Output: 26000  
	There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
	Let the input 4 matrices be A, B, C and D. The minimum number of 
	multiplications are obtained by putting parenthesis in following way
	(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30
	"""
	n = len(P)
	M = [[0 for j in range(n)] for i in range(n)]
	for i in range(1, n):
		M[i][i] = 0

	for sublen in range(2, n + 1):
		for i in range(1, n - sublen + 1):
			j = i + sublen - 1

			M[i][j] = float("inf")

			for k in range(i, j): 
				M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + P[i - 1] * P[k] * P[j])
	
	return M[1][-1]

print matrix_chain_order([40, 20, 30, 10, 30])
