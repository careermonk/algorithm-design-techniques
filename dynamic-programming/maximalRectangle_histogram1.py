# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def maxRectangleAreaOneRow(height):
	stack=[]; i=0; maxArea=0
	while i<len(height):
		if stack==[] or height[i]>height[stack[-1]]:
			stack.append(i)
		else:
			curr=stack.pop()
			width=i if stack==[] else i-stack[-1]-1
			maxArea=max(maxArea,width*height[curr])
			i-=1
		i+=1
	while stack!=[]:
		curr=stack.pop()
		width=i if stack==[] else len(height)-stack[-1]-1
		maxArea=max(maxArea,width*height[curr])
	return maxArea

def maximalRectangle(matrix):
	m=len(matrix)
	n=len(matrix[0])
	heights = [[0 for j in range(n+1)] for i in range(m+1)]
	for i in range(m):
		for j in range(n):
			if matrix[i][j] is 1:
				heights[i][j]=1+heights[i-1][j]
	maxArea = 0
	currArea=-1
	for i in range(m):
		currArea = maxRectangleAreaOneRow(heights[i])
		maxArea = max(currArea, maxArea)

	return maxArea

matrix=[ [1,1,0,0,1,0],
    [0,1,1,1,1,1],
    [1,1,1,1,1,0],
    [0,0,1,1,0,0]
    ]
print maximalRectangle(matrix)
