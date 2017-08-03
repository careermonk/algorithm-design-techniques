def cut_rod(prices, rodSize):
	r = (rodSize + 1) * [None]
	
	def func(p, n):
		# use known answer, if one exists
		if r[n] is not None:
			return r[n]

		# otherwise use original recursive formulation
		if n == 0:
			q = 0
		else:
			q = float('-inf')
			# Consider a first cut of length i, for i from 1 to n inclusive
			for i in range(1, n+1):
				q = max(q, p[i] + func(p, n-i))   # recur on length n-i

		# memoize answer in table before returning
		r[n] = q
		return q
	return func(prices, rodSize)

p = [0, 2, 8, 10, 12]
print  cut_rod(p, len(p)-1)
