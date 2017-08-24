# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def maximalRectangle(matrix):
	m = len(matrix)
	if(m == 0):
		return 0
	maxArea = 0
	n = len(matrix[0])
	for mFrom in range(m):
		for mTo in range(mFrom, m):
			for nFrom in range(n):
				for nTo in range(nFrom, n):
					if(isValid(matrix, nFrom, nTo, mFrom, mTo)):
						maxArea = max(maxArea, getArea(nFrom, nTo, mFrom, mTo))
        return maxArea

def  getArea( nFrom,  nTo,  mFrom,  mTo):
	return (nTo - nFrom + 1) * (mTo - mFrom + 1)
    
def isValid(matrix,  nFrom,  nTo,  mFrom, mTo):
	for i in range(mFrom, mTo+1):
		for j in range(nFrom,  nTo+1):
			if(matrix[i][j] != 1):
				return False
        return True
	
matrix=[	[1,  1,  0,  0,  1, 0], 
		[0,  1,  1,  1,  1, 1], 
		[1,  1,  1,  1,  1, 0], 
		[0,  0,  1,  1,  0, 0]]

print maximalRectangle (matrix)
