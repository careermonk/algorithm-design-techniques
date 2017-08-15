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
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def solution(self):
        m, n =  len(self.matrix), len(self.matrix[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and self.matrix[i][j] == 1:
                    self.cur_region_size = 0
                    self.region_size(visited, i, j, m, n)
        return self.max

    def region_size(self, visited, i, j, m, n):
        visited[i][j] = True
        self.cur_region_size += 1
        self.max = max(self.max, self.cur_region_size)
	
	# for each of the neighbors, if it is not visited, call the funcion recursively and add the counts.
        for dir in self.directions:
            i1 = i + dir[0]
            j1 = j + dir[1]
            if 0 <= i1 < m and 0 <= j1 < n and not visited[i1][j1] and self.matrix[i1][j1] == 1:
                self.region_size(visited, i1, j1, m, n)


if __name__ == "__main__":
    matrix = [[1,1,0,0,0],
		[0,1,1,0,0],
		[0,0,1,0,1],
		[1,0,0,0,1],
		[0,1,0,1,1]]
    # region_size
    s = ConnectedCells(matrix)
    print "%s\n" % (s.solution())
