# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def path_finder( matrix , position , n ):
	# returns a list of the paths taken
	if position == ( n - 1 , n - 1 ):
		return [ ( n - 1 , n - 1 ) ]

	i , j = position
	# check whether we can move in the right direction
	if i + 1 < n and matrix[i+1][j] == 1:
		a = path_finder( matrix , ( i + 1 , j ) , n )
		if a != None:
			return [ (i , j ) ] + a

	# check whether we can move in the down direction
	if j + 1 < n and matrix[i][j+1] == 1:
		b = path_finder( matrix , (i , j + 1) , n )
		if  b != None:
			return [ ( i , j ) ] + b

matrix = [[ 1 , 1 , 1, 1 , 0], 
	     [ 0 , 1 , 0, 1 , 0], 
	     [ 0 , 1 , 0, 1 , 0], 
	     [ 0 , 1 , 0, 0 , 0], 
	     [ 1 , 1 , 1, 1 , 1] ]

print path_finder(matrix, (0,0), 5)
