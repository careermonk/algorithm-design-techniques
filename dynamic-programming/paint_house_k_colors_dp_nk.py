# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def paint_house_k_colors_dp(costs):
	n = len(costs)
	k = len(costs[0])
	if n < 1:
		return None
	elif n == 1:
		return min(costs[0])

	C = [[float("inf") for j in range(k)] for i in range(n)]

	previous_min, previous_second_min, previous_color = 0,  0, -1

	# calculate mininum cost to paint n houses
	for i in range(0, n):
		current_min, current_second_min, current_color= float("inf"), float("inf"),-1

		for j in range(0, k):

			temp_cost = costs[i][j] + (previous_second_min if previous_color==j else previous_min)

			if temp_cost<current_min:
				current_second_min = current_min
				current_min = temp_cost
				current_color = j
			elif temp_cost<current_second_min:
				current_second_min = temp_cost

		previous_min = current_min
		previous_second_min = current_second_min
		previous_color = current_color

	return previous_min

print paint_house_k_colors_dp([[13,	2,	10], [10,	13, 	5], [13,	4,	9]])
