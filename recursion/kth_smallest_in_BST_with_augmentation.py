'''Binary Search Tree Node'''
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data
        root.leftnodes = 1 #nodes on left including current node
        
# Modified BST insert that keeps track on #left nodes
def insert_bst(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            root.leftnodes += 1 #nodes on left including current node
            if root.left == None:
                root.left = node
            else:
                insert_bst(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert_bst(root.right, node)

# modified in-order traversal
def kth_smallest_in_BST(root, k):
    if (k < root.leftnodes):
        return kth_smallest_in_BST(root.left, k)
    elif (k > root.leftnodes):
        return kth_smallest_in_BST(root.right, k-root.leftnodes)
    else:
       return root.data
        
# create BST    
root = BSTNode(4)
input = [3, 2, 1, 6, 5, 8, 7, 9, 10, 11]
for x in input:
    insert_bst(root, BSTNode(x))


print kth_smallest_in_BST(root, 1)
print kth_smallest_in_BST(root, 5)
print kth_smallest_in_BST(root, 10)
