
# Divide and conquer technique
def max_max(A):
  if len(A) == 1:          # if A contains only 1 item
    return (-1, A[0])      # return -1 (a dummy item) and that item

  elif len(A) == 2:        # if A contains only 2 items
    if A[0] <= A[1]:       # find which is min and which
      return (A[0], A[1])  # is max, and return them
    else:
      return (A[1], A[0])

  else:                                				# general case
    mid = len(A) / 2
    (max1_left, max2_left) = max_max(A[:mid])   	# recursively find 2 maximal items in left half of A
    (max1_right, max2_right) = max_max(A[mid:])   	# recursively find 2 maximal items in right half of A
    if max2_left >= max2_right:                 		# assign the max of the two maximal items
      max2 = max2_left                     			# to max2 (in this case, max2_left) and assign the other
      max1 = max2_right                    			# maximal item (max2_right in this case( to max1 
      if max1_left > max1:                 			# now we know that max1_right cannot be the second maximum
        max1 = max1_left                   			# so just check if max1_left is bigger than max2_right
    else:
      max2 = max2_right
      max1 = max2_left
      if max1_right > max1:
        max1 = max1_right
    
    return (max1, max2)                			# return the overall maximal items

A = [3, 4, 29, 41, 45, 49, 79, 89]
print max_max(A)

# Iterative technique
def max_max_iterative(A):
  if len(A) == 1:          					# if A contains only 1 item
    return (-1, A[0])      					# return -1 (a dummy item) and that item

  elif len(A) == 2:        					# if A contains only 2 items
    if A[0] <= A[1]:       					# find which is min and which
      return (A[0], A[1])  					# is max, and return them
    else:
      return (A[1], A[0])
  else:
    if A[0] <= A[1]:
    	max1 = A[0]
    	max2 = A[1]
    else:
    	max1 = A[1]
    	max2 = A[0]
    index = 2
    while index < len(A):
    	if A[index] > max2:
    		max1 = max2
    		max2 = A[index]
    	elif A[index] > max1:
    		  max1 = A[index]
    	index = index + 1
    return (max1, max2)
	
print max_max_iterative(A)
  
