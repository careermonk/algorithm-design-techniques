# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

'''Binary Search Tree Node'''
class BSTNode:
    def __init__(self, data):
        self.data = data 		#root node
        self.left = None 		#left child
        self.right = None 	     #right child

def k_smallest(root, k):
	result = []
	def funct(root):
		if(not root): 
			return
		if len(result) >= k:
			return 
		funct(root.left)
		result.append(root.data)
		funct(root.right)
	funct(root)
	return result

node1, node2, node3, node4, node5, node6 = \
BSTNode(6), BSTNode(3), BSTNode(8), BSTNode(1), BSTNode(4), BSTNode(7)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left = node6

result = k_smallest(node1, 3)
print result
