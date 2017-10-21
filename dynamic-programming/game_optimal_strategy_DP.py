# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def game(coins):
	n = len(coins)
	V = [[0 for i in range(n)] for j in range(n)]
	#Initialize for length=1
	for i in range(n):
		V[i][i] = coins[i]

	#Generate coins for length=2, 3 ....
	#size+1 to include all coins!	
	for l in range(2, n+1):
		#start value range 0  & 1
		for i in range(0, n):
			#end coins changes based on i and length(l)
			#size =2  -> [0, 1] [1, 2],[2, 3]
			#size =3  -> [0, 2], [1, 3]
			j = i + l - 1

			#IMPORTANT: break when i or j index is not valid
			if i >= n or i+1 >= n or i+2 >= n or j >= n:
				break

			#option 1: pick i	
			path1 = coins[i] + min(V[i+2][j],V[i+1][j-1])

			#option 2: pick j
			path2 = coins[j] + min(V[i+1][j-1],V[i][j-2])
			V[i][j] = max(path1, path2)
	#print(V)
	return V[0][n-1]

# row of n coins
coins = [4,  3,  3,  4,  2,  3]
print game(coins)
