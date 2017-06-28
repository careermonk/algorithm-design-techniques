# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def lucky_memoization(m):
	'''Using memoization and using a dictionary as a table.'''
	table = {}
	def lucky(n):
		if n not in table:
			if n == 0:
				table[n] = 0
			elif n == 1:
				table[n] = 1
			else:
				table[n] = 10*lucky(n-1) - lucky(n-2)
		return table[n]
	return lucky(m)

print lucky_memoization(3)
