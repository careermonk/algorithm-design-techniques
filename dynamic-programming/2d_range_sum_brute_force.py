class RangeSum(object):
	def __init__(self, matrix):
		self.m = len(matrix)
		self.n = len(matrix[0]) if self.m else 0
		self.cumulative_sums = [[0] * (self.n + 1) for i in range(self.m + 1)]
	
		self.__pre_compute(matrix)

	def __pre_compute(self, matrix):
		for i in range(self.m):
			for j in range(self.n):
				self.cumulative_sums[i+1][j+1] = self.cumulative_sums[i+1][j] + \
			self.cumulative_sums[i][j+1] + matrix[i][j] - self.cumulative_sums[i][j]

	def range_sum(self, row1, col1, row2, col2):
		return self.cumulative_sums[row2 + 1][col2 + 1] + self.cumulative_sums[row1][col1] \
				- self.cumulative_sums[row1][col2 + 1] - self.cumulative_sums[row2 + 1][col1]

matrix = [
  [3, 0, 1, 4, 2],
  [4, 6, 3, 2, 1],
  [1, 2, 9, 1, 5],
  [4, 1, 2, 1, 7],
  [1, 0, 3, 0, 5]
]

mtx  = RangeSum (matrix)
print mtx.range_sum(1, 2, 3, 4)
