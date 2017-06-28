# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def paint_house_min_cost_dp(costs):
    n = len(costs)
    if n < 1:
        return None
    elif n == 1:
        return min(costs[0])

    C = [[0 for j in range(3)] for i in range(n)]
    C[0] = costs[0]

    # calculate mininum cost to paint n houses
    for i in range(1, n):
    	# painting ith house with red: hence we have select blue or green for i-1 house
        C[i][0] = min(C[i - 1][1] + costs[i][0], C[i - 1][2] + costs[i][0])

       	# painting ith house with blue: hence we have select red or green for i-1 house
        C[i][1] = min(C[i - 1][0] + costs[i][1], C[i - 1][2] + costs[i][1])

       	# painting ith house with green: hence we have select red or blue for i-1 house
        C[i][2] = min(C[i - 1][0] + costs[i][2], C[i - 1][1] + costs[i][2])
	print C
    return min(C[n - 1])


print paint_house_min_cost_dp([[13,	2,	10], [10,	13, 	5], [13,	4,	9]])
