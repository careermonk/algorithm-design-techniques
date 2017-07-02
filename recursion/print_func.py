def print_func(n):
	if n == 0: 								# this is the terminating base case
	    return 0
	else:
 	    print n
	    return print_func(n-1)       		# recursive call to itself again

print(print_func(4)) 
