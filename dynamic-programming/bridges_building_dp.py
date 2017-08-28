# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def lis(A):
	LIS = [1 for _ in range(len(A))]
	for i in range(len(A)):
		for j in range(i):
			if A[j] <= A[i]:
				LIS[i] = max(LIS[i], LIS[j] + 1)

	## trace subsequence back to output
	result = []
	element = LIS[len(LIS)-1]
	for i in  range(len(LIS)-1, -1, -1):
		if LIS[i] == element:
			result.append(A[i])
			element -=  1

	return list(result.__reversed__())

l_cities = [6, 2, 5, 1, 8, 7, 4, 3]
r_cities = [5, 1, 8, 3, 4, 2, 6, 7]
l_cities.sort()
bridges = lis(r_cities)
for i in range(len(bridges)):
    print "Adding bridge:", bridges[i], "-->", bridges[i]
