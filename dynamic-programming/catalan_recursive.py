# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def catalan_recursive(n):
  if n == 0:
    return 1
  else:
    count = 0
    for i in range(n):
      count += catalan_recursive(i) * catalan_recursive(n - 1 - i)
  return count

print catalan_recursive(3)
