
# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def cut_rod(p, n):
	r = (n + 1) * [0]
	cuts = (n + 1) * [0]
	for j in range(1, n+1):
		q = float('-inf')
		for i in range(1, j+1):
			if q < p[i] + r[j-i]:
				q = p[i] + r[j-i]
				cuts[j] = i
		r[j] = q
	revenue = r[n]
	pieces = []
	while n > 0:	
		pieces.append(cuts[n])
		n = n - cuts[n]         # continue on what remains
	return revenue, pieces

p = [0, 2, 8, 10, 12]
print  cut_rod(p, len(p)-1)
