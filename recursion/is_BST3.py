'''Binary Search Tree Node'''
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def is_BST(root, min, max):
	if root is None:
		return True
	if root.data<=min or root.data>=max:
		return False
	result = is_BST(root.left, min, root.data)
	result = result and is_BST(root.right, root.data, max)
	return result

# create BST    
node1, node2, node3, node4, node5 = \
BSTNode(6), BSTNode(2), BSTNode(8), BSTNode(1), BSTNode(9)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
root = node1
print is_BST(root, float("-infinity"), float("infinity"))  

# create BST    
node1, node2, node3, node4, node5 = \
BSTNode(9), BSTNode(2), BSTNode(10), BSTNode(1), BSTNode(6)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
root = node1
print is_BST(root, float("-infinity"), float("infinity"))  
