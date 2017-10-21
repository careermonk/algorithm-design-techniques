# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def expand(S,  left, right):
	n = len(S)
	while (left >= 0 and right < n and S[left] == S[right]):
		left -= 1
		right += 1
  
	return S[left+1:right]
 
def LPS(S) :
	n = len(S)
	if (n == 0): 
		return ""
	if (n == 1): 
		return S

	longest = ""

	for i in range(n):
		# get longest palindrome with center of i
		p1 = expand(S, i, i)
		if (len(p1) > len(longest)):
			longest = p1

		# get longest palindrome with center of i, i+1
		p2 = expand(S, i, i+1)
		if (len(p2) > len(longest)):
			longest = p2
  
	return longest

S = "abaccddccefeg"
lps = LPS(S)
print lps, len(lps)
