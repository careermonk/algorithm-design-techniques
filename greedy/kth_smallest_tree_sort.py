# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

'''Binary Search Tree Node'''
class BSTNode:
    def __init__(self, data):
        self.data = data 		#root node
        self.left = None 		#left child
        self.right = None 	     #right child

def kth_smallest(root, k):
	global count
	count = 0
	def funct(root):
		global count
		if(not root): 
			return None

		left = funct(root.left)
		if(left): 
			return left

		count += 1
		if(count == k): 
			return root.data

		return funct(root.right)

	return funct(root)

node1, node2, node3, node4, node5, node6 = \
BSTNode(6), BSTNode(3), BSTNode(8), BSTNode(1), BSTNode(4), BSTNode(7)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left = node6

print kth_smallest(node1, 3)
