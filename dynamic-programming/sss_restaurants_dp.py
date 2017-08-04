# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def sss_restaurants(distances, profit, k):
	n = len(distances)-1
	M = (n + 1) * [0]
	for i in range(1, n+1):
		q = M[i-1]
		for j in range(0, i+1):
			if( distances[j] <= distances[i]-k):
				q = max(q, profit[i] + M[j])
		M[i] = q
	return M[n]

distances = [0, 2, 4, 5, 6, 6]
profits = [0, 10, 20, 40, 80, 100]
print sss_restaurants(distances, profits, 2)
