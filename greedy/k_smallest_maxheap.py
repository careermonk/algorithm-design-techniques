# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

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

	def maximum (self):
		if self.size >=1:
			return self.A[1]
		return None

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

	def k_smallest(self, A, k):
		self.build_heap(A[:k])
		result = []
		for X in range(k, len(A)):
			m = self.maximum()
			if A[X] < m:
				self.delete_max()
				self.insert(A[X])

		while self.size > 0:
			result.append(self.delete_max())
		return result

h = MaxHeap()
print h.k_smallest([10, 5, 1, 6, 20, 19, 22, 29, 32, 29, 4], 5)
