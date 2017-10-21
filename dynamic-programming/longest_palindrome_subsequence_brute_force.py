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
	lps = ""

	def is_palindrome(str):
		if str == str[::-1] :
			return True

     # generates all subsets (powerset)
	def powerset(s):
		n = len(s)
		masks = [1<<j for j in xrange(n)]
		for i in xrange(2**n):
			yield [s[j] for j in range(n) if (masks[j] & i)]

	for subseq in powerset(S):
		if is_palindrome(subseq) and (len(subseq) > len(lps)):
			lps = subseq
	return lps

lps = longest_palindrome_subsequence("abaccddccefeg")
print lps, len(lps)
