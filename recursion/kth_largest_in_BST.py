'''Binary Search Tree Node'''
class BSTNode:
    def __init__(self, data):
        self.data = data 		#root node
        self.left = None 		#left child
        self.right = None 		#right child

count=0
def kth_largest_in_BST(root, k):
	global count
	if(not root): 
	    return None
	right = kth_largest_in_BST(root.right, k)
	if( right ): 
		return right
	count += 1
	if(count == k): 
		return root
	return kth_largest_in_BST(root.left, k)

node1, node2, node3, node4, node5, node6 = BSTNode(6), BSTNode(3), BSTNode(8), BSTNode(1), BSTNode(4), BSTNode(7)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left = node6


count=0
result = kth_largest_in_BST(node1, 3)
print result.data

count=0
result = kth_largest_in_BST(node1, 5)
print result.data

count=0
result = kth_largest_in_BST(node1, 2)
print result.data
