def minimum_dot_product(X, Y):
	X.sort()
	Y.sort(reverse=True)
	print X, Y
	min_product = 0
	for i in range( len(X) ):
		min_product += X[i]*Y[i]
        return min_product

X = [1, 2, -4]
Y = [-2, 4, 1]

print minimum_dot_product(X, Y)
