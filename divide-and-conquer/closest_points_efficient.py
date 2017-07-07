from math import sqrt, pow
def closest_points(S):
	def distance(p,q): 
		return pow(p[0] - q[0],2) + pow(p[1] - q[1],2)	

	# We use the pair S[0],S[1] as our initial guess at a small distance.
	result_pair = [distance(S[0],S[1]), (S[0],S[1])]
	
	# check whether pair (p,q) forms a closer pair than one seen already
	def check_pair(p,q):
		d = distance(p,q)
		if d < result_pair[0]:
			result_pair[0] = d
			result_pair[1] = p,q
			
	# merge two sorted lists by x-coordinate
	def merge(S1,S2):
		i = 0
		j = 0
		while i < len(S1) or j < len(S2):
			if j >= len(S2) or (i < len(S1) and S1[i][1] <= S2[j][1]):
				yield S1[i]
				i += 1
			else:
				yield S2[j]
				j += 1

	# Find closest pair recursively; returns all points sorted by x coordinate
	def recur(S):
		if len(S) < 2:
			return S
		# Since the values were sorted by x coordinate, middle element is the median
		mid = len(S)/2
		midian_x_value = S[mid][0]
		S1 = S[:mid]
		S2 = S[mid:]
		S = list(merge(recur(S1), recur(S2)))

		E = [p for p in S if abs(p[0]-midian_x_value) < result_pair[0]]
		for i in range(len(E)):
			for j in range(1,8):
				if i+j < len(E):
					check_pair(E[i],E[i+j])
		return S
	S.sort()
	recur(S)
	return result_pair[1]

print closest_points([(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),\
			  (19,7),(14,22),(8,19),(7,29),(10,11),(1,13)])
