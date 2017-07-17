class DisjointSet:   
	def __init__(self, n):
	      self.MAKESET(n)

	def MAKESET(self, n):
	      self.S = [-1 for x in range(n)]
	
	def FIND(self, X):
		if( self.S[X] < 0 ): 
		      return X
		else:	
		      return self.FIND(self.S[X])

	def UNION(self, root1, root2):
		if self.FIND(root1) == self.FIND(root2):
			return		
		if(self.S[root1]  < self.S[root2] ):
			self.S[root2] = root1
		elif self.S[root1] == self.S[root2] :
			self.S[root2] = self.S[root2] - 1
			self.S[root1] = root2
		else:
			self.S[root1] = root2

		print self.S
ds = DisjointSet(7)
ds.UNION(5, 6)
ds.UNION(1, 2)
ds.UNION(0, 2)

print ds.FIND(5), ds.FIND(1), ds.FIND(2)
