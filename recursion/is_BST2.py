'''Binary Search Tree Node'''
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def find_min(root):
	current = root
	if current is None:  
		return None
	while current.left is not None:
		current = current.left
	return current

def find_max(root):
	current = root
	if current is None:  
		return None
	while current.right is not None:
		current = current.right
	return current


       # Returns true if a binary tree is a binary search tree 
def is_BST(root):
	if root is None:
		return True

	# false if the max of the left is > than root 
	max_element = find_max(root.left)
	if root.left is not None and max_element.data > root.data:
		return False

	# false if the min of the right is <= than root 
	min_element = find_min(root.right)
	if root.right is not None and min_element.data < root.data:
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

# create BST    
node1, node2, node3, node4, node5 = \
BSTNode(9), BSTNode(2), BSTNode(10), BSTNode(1), BSTNode(6)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
root = node1
print is_BST(root)
