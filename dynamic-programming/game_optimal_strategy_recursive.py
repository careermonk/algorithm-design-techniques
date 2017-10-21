# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def game(coins, i, j):
	#exit condition, i > j (not i == j)
	if i > j:
		return 0
	else:
		#Each player leaves the minimum value
		path1 = coins[i] + min(game(coins, i+2, j), game(coins, i+1, j-1))
		path2 = coins[j] + min(game(coins, i+1, j-1), game(coins, i, j-2))
		return max(path1,path2)

# row of n coins
coins = [4, 3, 3, 4, 2, 3]
print game(coins, 0, len(coins)-1)
