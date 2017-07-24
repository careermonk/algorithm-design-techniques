from random import randint
def knapsack(weights, values, C):
	n = len(weights)
	V = [[0 for x in range(C+1)] for x in range(n+1)]

	for i in range(1, n+1):
		for j in range(C+1):
			if weights[i-1] > j:
				# If this next item (i-1) won't fit into the V[i][j] solution,
				# then the best we have is the previous solution, without it.
				V[i][j] = V[i-1][j]
			else:
				# If the next item (i-1) might work, then take the best of
				# i) the previous solution without it, or
				# ii) the best solution without the weight of (i-1).
				V[i][ j] = max(V[i-1][ j], V[i-1][ j - weights[i-1]] + values[i-1])

	# At this point we have the matrix of all smaller solutions
	# and the value of the total solution.
	(value, j, items) = (V[n][C], C, [])

	for i in range(n, 0, -1):
		print('i={}, value={}, j={}, items={}'.format(i, value, j, items))
		if weights[i-1] <= j:
			if V[i-1][ j] < V[i-1][ j-weights[i-1]] + values[i-1]:
				(value, j, items) = (value - values[i-1], j - weights[i-1], items + [i-1])
	items.reverse()
	print 'The answer is items={}, value={}.'.format(items, V[n][C])
	

def main():
	n = 6

	# Generate a sample problem.
	# 1. Random weights and values
	(min_weight, max_weight, min_value, max_value) = (2,20, 10,50)
	weights = map(lambda x: randint(min_weight, max_weight), range(n))
	values = map(lambda x: randint(min_weight, max_weight), range(n))

	# 2. An arbitrary but consisten C.
	C = sum(weights)/2            # 
	template = ' {:6}  {:6}  {:6}'
	print template.format('item', 'weight', 'value')
	print template.format('-'*8, '-'*8, '-'*8)
	for i in range(n):
		print template.format(i, weights[i], values[i])

	knapsack(weights, values, C)
if __name__ == '__main__':
    main()
