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
	lps = ""

	def is_palindrome(str):
	    if str == str[::-1] :
		return True

	for idX, item in enumerate(S):
		for idY, item in enumerate(S):
			subStr = S[idX:idY+1]
			if is_palindrome(subStr) and (len(subStr) > len(lps)):
				lps = subStr
	return lps

lps = LPS("abaccddccefeg")
print lps, len(lps)
