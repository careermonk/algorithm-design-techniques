# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def n_choose_m(n , m):
	if m == 0 or m == n :
		return 1

	# Recursive Call
	return n_choose_m(n-1 , m-1) + n_choose_m(n-1 , m)

print(n_choose_m(5,2)) # 10
