# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def LCS(X, Y, i, j):
    if i == -1 or j == -1:
        return 0
    if X[i] == Y[j]:
        return 1 + LCS(X, Y, i-1, j-1)
    return max(LCS(X, Y, i-1, j), LCS(X, Y, i, j-1))

X = 'thisisatest'
Y = 'testingLCS123testing'
print (LCS(X, Y, len(X)-1, len(Y)-1))
