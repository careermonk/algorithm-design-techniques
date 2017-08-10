# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def permutations(S):
	soFar = []  # initially nothing is placed in it
	B = S # initially B contains everything
	for perm in genPerms(soFar, B):
		print perm

def genPerms(soFar, B):
	# Base case: If there are no more elements to permute, then the answer will
	# be the permutation we have created so far.
	if len(B) == 0:
		yield soFar

	# Otherwise, try extending the permutation we have so far by each of the
	# elements we have yet to permute.
	else:
		for x in range(0, len(B)):
			# First parameter: Place the element from B into position m+1 in perms
			# Second parameter: Make a temporary copy of B without the element x
			# Extend the current permutation by the xth element, then remove
			# the xth element from the set of elements we have not yet
			# permuted. We then iterate across all the permutations that have
			# been generated this way and hand each one back to the caller.
			for perm in genPerms(soFar + [B[x]], B[0:x] + B[x+1:]):
				yield perm

permutations(['A', 'B', 'C', 'A'])
