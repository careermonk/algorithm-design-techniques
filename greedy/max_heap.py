class MaxHeap:
	def __init__(self):
		self.A = [0]
		self.size = 0

	def percolate_up(self,i):
		while i // 2 > 0:
			if self.A[i] > self.A[i // 2]:
				tmp = self.A[i // 2]
				self.A[i // 2] = self.A[i]
				self.A[i] = tmp
			i = i // 2

	def insert(self,k):
		self.A.append(k)
		self.size = self.size + 1
		self.percolate_up(self.size)

	def percolate_down(self,i):
		while (i * 2) <= self.size:
			maxChild = self.max_child(i)
			if self.A[i] < self.A[maxChild]:
				tmp = self.A[i]
				self.A[i] = self.A[maxChild]
				self.A[maxChild] = tmp
			i = maxChild

	def max_child(self,i):
		if i * 2 + 1 > self.size:
			return i * 2
		else:
			if self.A[i*2] < self.A[i*2+1]:
				return i * 2 + 1
			else:
				return i * 2

	def delete_max(self):
		retval = self.A[1]
		self.A[1] = self.A[self.size]
		self.size = self.size - 1
		self.A.pop()
		self.percolate_down(1)
		return retval

	def build_heap(self, A):
		i = len(A) // 2
		self.size = len(A)
		self.A = [0] + A[:]
		while (i > 0):
			self.percolate_down(i)
			i = i - 1

	def k_smallest(self, k):
		result = []
		for i in range(k):
			result.append(self.delete_max())
		return result


h = MaxHeap()
h.build_heap([10, 5, 1, 6, 20, 19, 22, 29, 32, 29, 4])
print h.k_smallest(3)
