def n_choose_k(n , k):
	if (k > n or k < 0):
		return None
	# declaring a row of Pascal triangle
	C = [0 for i in range(k+1)]

	# base case
	C[0] = 1 

	for i in range(1,n+1):
		# Compute next row of pascal triangle using the previous row
		j = min(i ,k)
		while (j>0):
			C[j] = C[j] + C[j-1]
			j -= 1
	return C[k]
 
print(n_choose_k(5,2)) # 10
