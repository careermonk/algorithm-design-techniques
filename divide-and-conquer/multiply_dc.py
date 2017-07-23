def multiply_dc(A,B):
	if len(str(A)) == 1 or len(str(B)) == 1:
		return A*B

	n = max(len(str(A)), len(str(B)))
	#calculates the size of the numbers in base 10
	m=max(len(str(A)), len(str(B)))//2

	#split the digit sequences about the middle
	cut=pow(10,m)
	a_left, a_right=A//cut, A%cut
	b_left, b_right=B//cut, B%cut

	#divide and conquer
	p1=multiply_dc(a_left, b_left)
	p2=multiply_dc(a_left, b_right)
	p3=multiply_dc(a_right, b_left)
	p4=multiply_dc(a_right, b_right)

	return p1*pow(10, 2*m) + (p2+p3)*pow(10, m) + p4

print multiply_dc(523, 523)
