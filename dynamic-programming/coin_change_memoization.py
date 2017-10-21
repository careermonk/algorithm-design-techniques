# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def make_change(C, denominations, memo):
    if C == 0:
        return 0

    if C in memo:
        return memo[C]

    min_coins = float("inf")
    for i in range(len(denominations)):
        coin = denominations[i]
        if coin > C:
            continue
        val = make_change(C - coin, denominations, memo)
        min_coins = min(min_coins, val)

    min_coins += 1

    memo[C] = min_coins
    return min_coins

print make_change(40, [1, 5, 10, 20, 25, 50], {})
