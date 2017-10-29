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

	C = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
	for j in xrange(n+1):
	    C[0][j] = 0
	for i in xrange(m+1):
	    C[i][0] = 1

	for i in xrange(1, m+1):
	    for j in xrange(1, n+1):
		if S[i-1]==T[j-1]:
		    C[i][j] = C[i-1][j]+C[i-1][j-1]
		else:
		    C[i][j] = C[i-1][j]

	return C[m][n]

print distinct_subsequences("abadcb", "ab")
