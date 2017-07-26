def get_boats(W, k):
	boats = 0
	j = 0
	i = len(W) - 1
	while (i >= j):
		if W[i] + W[j] <= k:
			j += 1
		boats += 1
		i -= 1
	return boats


W = (5, 20, 21, 28, 39, 40, 65, 89, 98, 105)
print get_boats(W, 110)
