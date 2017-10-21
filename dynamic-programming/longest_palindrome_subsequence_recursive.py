# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

# Returns the length of the longest palindromic subsequence in S
def LPS(S,  i,  j):
	# Base case: If there is only 1 character
	if (i == j):
		return 1

	# Base case: If there are only 2 characters and both are same
	if (S[i] == S[j] and i + 1 == j):
		return 2

	# If the first and last characters are same
	if (S[i] == S[j]):
		return LPS(S, i+1, j-1) + 2

	# If the first and last characters are not same
	return max( LPS(S, i, j-1), LPS(S, i+1, j) )

S = "abaccddccefeg"
lps = LPS(S, 0, len(S)-1)
print lps, len(lps)
