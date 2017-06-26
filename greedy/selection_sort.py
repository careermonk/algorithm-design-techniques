def selection_sort( A ):
  for i in range( len( A ) ):
    least = i
    for k in range( i + 1 , len( A ) ):
      if A[k] < A[least]:
        least = k
 
    swap( A, least, i )

def swap( A, x, y ):
  temp = A[x]
  A[x] = A[y]
  A[y] = temp
	      
A = [54,26,93,17,77,31,44,55,20]
selection_sort(A)
print(A)
