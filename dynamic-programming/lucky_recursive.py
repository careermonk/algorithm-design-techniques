# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def lucky(n):
    '''lucky implementation with recursion'''
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return 10*lucky(n-1) - lucky(n-2)

print lucky(3)
