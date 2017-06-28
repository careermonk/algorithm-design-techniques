# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

catalan=[]

#1st term is 1
catalan.append(1)

for i in range (1,1001):
  x=catalan[i-1]*(4*i-2)/(i+1)
  catalan.append(x)

def catalan_number(n):
  return catalan[n]

print catalan_number(3)
