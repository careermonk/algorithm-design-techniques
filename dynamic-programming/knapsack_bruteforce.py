from random import randint

def binary(i, digits):
	"""Return i as a binary string with given number of digits,
	padding with leading 0's as needed.
	>>> binary(0, 4)
	'0000'
	"""
	result = bin(i)[2:]   # Python's built-in gives e.g. '0b0'
	return '0'*(digits-len(result)) + result

def knapsack(weights, values, capacity):
	n = len(weights)
	count = 2**n
	(best_value, best_items, best_weight) = (0, [], 0)
	for i in xrange(count):
		i_base2 = binary(i, n)
		print ('i_base2 = {}'.format(i_base2))
		item_numbers = filter(lambda item: i_base2[item]=='1', range(n))
		print ('item numbers = {}'.format(item_numbers))
		weight = reduce(lambda w,item: w + weights[item], item_numbers, 0)
		print ('weight = {}'.format(weight))
		if weight <= capacity:
			value = reduce(lambda w,item: w + values[item], item_numbers, 0)
			print ('value = {}'.format(value))
			if value > best_value:
				(best_value, best_items, best_weight) = (value, item_numbers, weight)
				print ('best_value = {}'.format(best_value))
        print('  ---   ---   ---   ---   --- ')
	print 'The answer is item_numbers={}, value={}.'.format(best_items, best_value)

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

	knapsack(weights, values, capacity)
if __name__ == '__main__':
    main()
