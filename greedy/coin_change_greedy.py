# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def make_change(C):
    denominations = [10, 5, 1]  # must be sorted
    coins_count = 0
    for coin in denominations:
        # Update coins_count with the number of denominations 'are held' in the C.
        coins_count += C // coin
        # Put remainder to the residuary C.
        C %= coin

    return coins_count

print make_change(40)
