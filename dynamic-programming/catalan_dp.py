# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def catalan_dp(n):
	'''Using UP and using a dictionary as a table.'''
	catalan=[1,1]+[0]*n
	for i in range(2,n+1):
		for j in range(n):
			catalan[i]+=catalan[j]*catalan[i-j-1]
	return catalan[n]

print catalan_dp(3)
