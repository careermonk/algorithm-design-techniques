# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def unique_digits(n):
	if n == 0:
		return 0
	if n == 1:
		return 10
	count = 9
	for i in xrange(2, n+1):
		count = count * (10 - i + 1)
	return count

print unique_digits(2)
print unique_digits(3)
print unique_digits(4)
