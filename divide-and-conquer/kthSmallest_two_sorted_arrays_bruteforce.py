def kthSmallest(A, B, k):
	mergedList= []
	i=0; j=0
	m = len(A)
	n = len(B)
	while i < m and j < n:
		if(A[i]<B[j]):
			mergedList.append(A[i])
			i+=1
		else:
			mergedList.append(B[j])
			j+=1

	if(i<m):
		mergedList+=A[i:m]
	if(j<n):
		mergedList+=B[j:n]
	
	if k < len(mergedList):
		return mergedList[k-1] 
	else:
		return None
	
A = [1, 5, 8, 10, 50]
B = [3, 4, 29, 41, 45, 49]
print kthSmallest(A, B, 5)
