# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

class ConnectedCells(object):
	def __init__(self, matrix):
		self.max = -1
		self.matrix = matrix
		self.cur_region_size = 0
		self.m, self.n =  len(self.matrix), len(self.matrix[0])
		self.visited = [[False for _ in xrange(self.n)] for _ in xrange(self.m)]

	def solution(self):
		for i in xrange(self.m):
			for j in xrange(self.n):
				if not self.visited[i][j] and self.matrix[i][j] == 1:
					self.cur_region_size = self.region_size(i, j)
					self.max = max(self.max, self.cur_region_size)
		return self.max

	def region_size(self, i, j):
		if i < 0 or i >= self.m or j < 0 or j  >= self.n:
			return 0
		elif self.matrix[i][j] == 0 or self.visited[i][j] == True:
			return 0
		else:
			self.visited[i][j] = True
			self.cur_region_size = 1 + self.region_size( i-1, j-1 ) \
							+ self.region_size( i-1, j ) \
							+ self.region_size( i-1, j+1 ) \
							+ self.region_size( i, j+1 ) \
							+ self.region_size( i+1, j+1 ) \
							+ self.region_size( i+1, j ) \
							+ self.region_size( i+1, j-1 ) \
							+ self.region_size( i, j-1 )
			return self.cur_region_size

if __name__ == "__main__":
	matrix = [[1,1,0,0,0],
		[0,1,1,0,0],
		[0,0,1,0,1],
		[1,0,0,0,1],
		[0,1,0,1,1]]
	# region_size
	s = ConnectedCells(matrix)
	print "%s\n" % (s.solution())
