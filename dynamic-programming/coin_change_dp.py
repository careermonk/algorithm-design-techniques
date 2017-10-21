# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def print_coins(min_coins, denominations):
    start = len(min_coins) - 1

    if min_coins[start] == -1:
        print "No Solution Possible."
        return

    print "Coins:",
    while start != 0:
        coin = denominations[min_coins[start]]
        print "%d " % coin,
        start = start - coin
    
def make_change(denominations, C):
    cols = C + 1
    table =[0 if idx == 0 else float("inf") for idx in range(cols)]
    min_coins = [-1 for _ in range(C + 1)]

    for j in range(len(denominations)):
        for i in range(1, cols):
            coin = denominations[j]
            if i >= denominations[j]:
                if table[i] > 1 + table[i - coin]:
                    table[i] = 1 + table[i - coin]
                    min_coins[i] = j

    print_coins(min_coins, denominations)
    return table[cols - 1]

print make_change([1, 5, 10, 20, 25, 50], 40)
