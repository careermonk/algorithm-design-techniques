def count_fence_painting_ways(n, k):
	temp = 0
	previous_one = k
	previous_two = k*k
	if n == 0: return temp
	if n == 1: return previous_one
	if n == 2: return previous_two
	for i in range(3, n):
		current = (k - 1) * (previous_two + previous_one)
		previous_one = previous_two
		previous_two = current
	
	return current

print count_fence_painting_ways(5,4)
