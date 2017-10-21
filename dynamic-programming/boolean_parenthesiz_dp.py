# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def count_parenthesize(operands, operators,  n):
	F = [[0 for j in range(n)] for i in range(n)]
	T = [[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		if (operands[i] == '0'):
			F[i][i] = 1
		else:
			F[i][i] = 0
		if (operands[i] == '1'):
			T[i][i] = 1
		else:
			T[i][i] = 0
		
	for L in range(1, n):
		i = 0
		for j in range(L, n):
			T[i][j] = F[i][j] = 0
			for count in range(L):
				k = i + count
				totalIK = T[i][k] + F[i][k]
				totalKJ = T[k+1][j] + F[k+1][j]
				if (operators[k] == '&'):
					T[i][j] += T[i][k]*T[k+1][j]
					F[i][j] += (totalIK *totalKJ - T[i][k]*T[k+1][j])

				if (operators[k] == '|'):
					F[i][j] += F[i][k]*F[k+1][j]
					T[i][j] += (totalIK*totalKJ - F[i][k]*F[k+1][j])

				if (operators[k] == '^'):
					T[i][j] += F[i][k]*T[k+1][j] + T[i][k]*F[k+1][j]
					F[i][j] += T[i][k]*T[k+1][j] + F[i][k]*F[k+1][j]
			i = i + 1
	return T[0][n-1]

print count_parenthesize("1101", "|&^", 4)
