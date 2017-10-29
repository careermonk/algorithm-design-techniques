# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def distinct_subsequences(S, T):
	m = len(S)
	n = len(T)
	# Base conditions
	if (m==0):
		return 0
	if (n==0):
		return 1
	if (m==1 and n==1):
	    if (S[0]==T[0]):
		    return 1
	    else:
		    return 0

	if (S[m-1]==T[n-1]):
		return distinct_subsequences(S[:-1], T[:-1]) + distinct_subsequences(S[:-1], T)
	else:
		return distinct_subsequences(S[:-1], T)
 
print distinct_subsequences("abadcb", "ab")
