'''Binary Search Tree Node'''
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def is_BST(root):
	if root is None:
		return True
	# false if left is > than root 
	if root.left is not None and root.left.data > root.data:
		return False

	# false if right is < than root 
	if root.right is not None and root.right.data < root.data:
		return False

	# false if, recursively, the left or right is not a BST 
	if not is_BST(root.left) or not is_BST(root.right):
		return False

	# passing all that, it's a BST 
	return True

# create BST    
node1, node2, node3, node4, node5 = \
BSTNode(6), BSTNode(2), BSTNode(8), BSTNode(1), BSTNode(9)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5

root = node1
print is_BST(root)
