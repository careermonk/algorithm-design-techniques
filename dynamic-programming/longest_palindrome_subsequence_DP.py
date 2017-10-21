# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def longest_palindrome_subsequence(S):
	n = len(S)
	L =[[0 for x in range(n)] for x in range(n)]

	# palindromes with length 1
	for i  in range(0,n-1):
		L[i][i] = 1

	# palindromes with length up to j+1
	for k  in range(2,n+1):
		for i  in range(0,n-k+1):
			j = i+k-1
			if S[i] == S[j] and k == 2:
				L[i][j] = 2
			if S[i] == S[j]:
				L[i][j] = 2 + L[i+1][j-1]
			else:
				L[i][j] = max( L[i+1][j] , L[i][j-1] )
	
	#print L
	return L[0][n-1]

print  longest_palindrome_subsequence("Career Monk Publications")		
