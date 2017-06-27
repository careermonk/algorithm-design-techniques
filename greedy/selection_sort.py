# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2017-06-02 06:15:46 
# Last modification		: 2017-06-02 
# Modified by		        : Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				 warranty; without even the implied warranty of 
# 				 merchantability or fitness for a particular purpose. 

def selection_sort( A ):
	for i in range( len(A) ):
		least = i
		for j in range( i + 1 , len(A) ):
			if A[j] < A[least]:
				least = j
	
		A[least], A[i] = A[i], A[least]

A = [54, 26, 93, 17, 77, 31, 44 , 55, 20]
selection_sort(A)
print(A)
