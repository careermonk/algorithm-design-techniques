def catalan_dp(n):
	'''Using UP and using a dictionary as a table.'''
	catalan=[1,1]+[0]*n
	for i in range(2,n+1):
		for j in range(n):
			catalan[i]+=catalan[j]*catalan[i-j-1]
	return catalan[n]
      
print catalan_dp(3)
