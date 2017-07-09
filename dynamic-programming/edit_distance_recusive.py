def edit_distance (A, B):
    if (A == ""):
	    return len(B) # base case
    elif (B == ""):
	    return len(A) # base case
    else:
	    add_distance = edit_distance(A, B[:-1]) + 1
	    delete_distance = edit_distance(A[:-1], B) + 1
	    change_distance = editDistance(A[:-1], B[:-1]) 
		change_distance = change_distance + int(A[len(A)-1]!=B[len(B)-1])
	    return min(min(add_distance, delete_distance), change_distance)
print edit_distance("Ceil", "trials")
