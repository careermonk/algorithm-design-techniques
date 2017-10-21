# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def LPS(S):
	n = len(S)
	T = [[False]*n for x in range(n)]
	n = len(S)
	maxLen = 1
	maxStart = 0

	# T[i][i] = True
	for i in range(n):
	    T[i][i] = True

	# T[i][i+1] = True if S[i] == S[i+1]
	for i in range(n-1):
	    if S[i] == S[i+1]:
		T[i][i+1] = True
		maxLen = 2
		maxStart = i

	# T[i][j] = True if S[i]==S[j] and T[i+1][j-1] == True
	for length in range(3, n+1):
	    for i in range(n- length + 1):
		j = i + length - 1
		if S[i] == S[j] and T[i+1][j-1] == True:
		    T[i][j] = True
		    maxLen = length
		    maxStart = i
	return S[maxStart:maxStart+maxLen]

S = "abaccddccefeg"
lps = LPS(S)
print lps, len(lps)
