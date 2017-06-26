# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2017-06-02 06:15:46 
# Last modification		: 2017-06-02 
# Modified by		        : Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				 warranty; without even the implied warranty of 
# 				 merchantability or fitness for a particular purpose. 

def partition( A, pivot, start, end):
	i = start  # save for the counterpart's pivot
	for j in range(start, end):
		if A[j] < pivot:
			A[i], A[j] = A[j], A[i]
			i = i + 1
		elif A[j] == pivot:
			A[j], A[end] = A[end], A[j]
			j = j - 1

	# move the counterpart's pivot from start to left
	A[i], A[end] = A[end], A[i]

	return i

def match_nuts_bolts( nuts, bolts, start, end):

	if start >= end:
		return

	b_pivot= end #random(start, end+1)
	n_pivot = partition(nuts, bolts[b_pivot], start, end)
	partition(bolts, nuts[n_pivot], start, end)
	match_nuts_bolts(nuts, bolts, start, n_pivot)
	match_nuts_bolts(nuts, bolts, n_pivot+1, end)

	    
nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
assert len(nuts) == len(bolts)
match_nuts_bolts(nuts, bolts, 0, len(bolts)-1)
print nuts, bolts
