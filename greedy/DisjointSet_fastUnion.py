 class DisjointSet:   
	def __init__(self, n):
	    self.S = []
	    self.MAKESET(n)

	def MAKESET(self, n):
	    for x in range(n):
		    self.S.append(x)

	def FIND(self, X):
		if( self.S[X] == X ): 
			return X
		else:	
			return self.FIND(self.S[X])

	def UNION(self, root1, root2):
		self.S[root1] = root2

ds = DisjointSet(7)
ds.UNION(5, 6)
ds.UNION(1, 2)
ds.UNION(0, 2)

print ds.FIND(5), ds.FIND(1),  ds.FIND(2)
