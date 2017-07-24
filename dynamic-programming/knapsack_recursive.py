from random import randint
def knapsack(weights, values, capacity, i):
	# Base cases
	if i == 0 or capacity == 0 :
		return 0

	# return the maximum of two cases:
	# 1. ith item selected
	# 2. ith item not selected
	else:
		return max(values[i-1] + knapsack(weights, values, capacity - weights[i-1], i-1), \
					knapsack(weights, values, capacity, i-1))

def main():
	n = 6

	# Generate a sample problem.
	# 1. Random weights and values
	(min_weight, max_weight, min_value, max_value) = (2,20, 10,50)
	weights = map(lambda x: randint(min_weight, max_weight), range(n))
	values = map(lambda x: randint(min_weight, max_weight), range(n))

	# 2. An arbitrary but consisten capacity.
	capacity = sum(weights)/2            # 
	template = ' {:6}  {:6}  {:6}'
	print template.format('item', 'weight', 'value')
	print template.format('-'*8, '-'*8, '-'*8)
	for i in range(n):
		print template.format(i, weights[i], values[i])

	print knapsack(weights, values, capacity, n)
if __name__ == '__main__':
    main()
