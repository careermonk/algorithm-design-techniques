# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def pair_sum_k(A, K):
    A.sort()
    left = 0
    right = len(A) - 1; 
    while(left < right):
         if(A[left] + A[right] == K):
              print A[left], A[right]
              left += 1
         elif(A[left] + A[right] < K):
              left += 1
         else:
              right -= 1
    
A = [1, 2, 6, 3, 5, 7, 8, 4, 0, 6, 10, -8, 12]
pair_sum_k(A, 12)
