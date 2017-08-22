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
	rows = len(matrix)
	columns = len(matrix[0])
	maxsqlen = 0
	for i in range(rows):
		for j in range(columns):
			if (matrix[i][j] == 1) :
				sqlen = 1
				flag = True
				while (sqlen + i < rows and sqlen + j < columns and flag) :
					for k in range(j, sqlen + j + 1):
						if (matrix[i + sqlen][k] == '0') :
							flag = False
							break
					for k in range(i, sqlen + i + 1):
						if (matrix[k][j + sqlen] == 0) :
							flag = False
							break
					if (flag):
					    sqlen += 1

				if (maxsqlen < sqlen):
					maxsqlen = sqlen
        return maxsqlen

matrix=[[0,  1,  1,  0,  1], 
		[1,  1,  0,  1,  0], 
		[0,  1,  1,  1,  0], 
		[1,  1,  1,  1,  0], 
		[1,  1,  1,  1,  1], 
		[0,  0,  0,  0,  0]]
print maximalSquare(matrix)
