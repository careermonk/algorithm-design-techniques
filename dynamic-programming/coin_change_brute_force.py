# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def make_change(C, denominations):
    # Default to C value
    min_coins = C

    # check to see if the amount is 0
    if C == 0:
        return 0	
    # check to see if we have a single coin match (base case)
    elif C in denominations:
        return 1
    else:
        # for every coin value that is <= than C
        for i in [c for c in denominations if c <= C]:
            # recursive call (add a coin and subtract from the C)
            num_coins = 1 + make_change(C-i, denominations)

            # reset minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print make_change(79, [1, 5, 10, 20, 25, 50])
