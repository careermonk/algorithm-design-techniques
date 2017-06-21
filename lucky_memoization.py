def lucky_memoization(m):
	'''Using memoization and using a dictionary as a table.'''
	table = {}
	def lucky(n):
		if n not in table:
			if n == 0:
				table[n] = 0
			elif n == 1:
				table[n] = 1
			else:
				table[n] = 10*lucky(n-1) - lucky(n-2)
		return table[n]
	return lucky(m)
      
print lucky_memoization(3)
