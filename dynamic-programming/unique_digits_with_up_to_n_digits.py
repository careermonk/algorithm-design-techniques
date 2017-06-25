def unique_digits(n):
	if n == 0:
		return 0
	if n == 1:
		return 10

	total = 10
	count = 9
	for i in xrange(2, n+1):
		count = count * (10 - i + 1)
		total += count
	return total

print unique_digits(2)
print unique_digits(3)
