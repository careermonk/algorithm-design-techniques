import math
def power_divide_and_conquer(a, n):
	"""Divide and Conquer power algorithm"""

	# base case
	if n == 0: 
		return 1

	# base case
	if a == 0:
		return 0

	x = power_divide_and_conquer(a, math.floor(n/2))
	if n % 2 == 0: 
		return x * x
	else: 
		return a * x * x

print power_divide_and_conquer(2, 4)
print power_divide_and_conquer(2, 3)
