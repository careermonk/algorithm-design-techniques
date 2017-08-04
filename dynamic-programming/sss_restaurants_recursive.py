def sss_restaurants(distances, profit, i, k):
	def funct(i):
		if i == 0:
			return 0
		else:
			q = funct(i-1)
			for j in range(i-1, -1, -1): 
				if( distances[j] < distances[i]-k):
					q = max(q, profit[i]+funct(j))
			return q
	return funct(i)

distances = [0, 2, 4, 5, 6]
profits = [0, 10, 20, 40, 80]
print sss_restaurants(distances, profits, len(distances)-1, 1)
