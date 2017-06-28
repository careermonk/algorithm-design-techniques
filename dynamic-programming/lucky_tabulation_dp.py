# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def lucky_tabulation_dp(n):
    '''Using DP and using a dictionary as a table.'''
    table = {}
    for i in range(n+1):
      if i == 0:
          table[i] = 0
      elif i == 1:
          table[i] = 1
      else:
          table[i] = 10*table[i-1] - table[i-2]
    return table[n]

print lucky_tabulation_dp(3)
