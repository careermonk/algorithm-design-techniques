global max_lis_length  
def lis(A, i): 
	# Declaration to allow modification of the global copy of max_lis_length
	global max_lis_length 

	# Base case 
	if i == 0: 
		return 1 
	max_lis_with_ith_element = 1 
	for j in xrange(0, i): 
		if A[j] < A[i]: 
			max_lis_with_ith_element = max(max_lis_with_ith_element, 1 + lis(A, j) ) 
	# Check if currently calculated LIS ending at 
	# A[i] is longer than the previously calculated 
	# LIS and update max_lis_length accordingly 
	if (max_lis_length < max_lis_with_ith_element): 
		max_lis_length = max_lis_with_ith_element

	return max_lis_with_ith_element 

# Test code 
def main(): 
	# Following declaration is needed to allow modification 
	# of the global copy of max_lis_length in lis() 
	global max_lis_length 
	max_lis_length = 1 
	A = [5, 8, 9, 20, 14, 2, 7, 19] 
	print "Length of LIS is", lis(A, len(A)-1) 
if __name__=="__main__": 
	main()
