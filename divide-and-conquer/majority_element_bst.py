class BSTNode:
    '''A node in a binary search tree. Has left and right subtrees.'''
    def __init__(self, data, left=None, right=None):
		self.left = left
		self.right = right
		self.data = data
		self.count = 1

class BinarySearchTree:
    '''Representes a binary search tree.'''
    
    def __init__(self):
		'''Create a new search tree.'''
		self.root = None
		self.size = 0


    def insert(self, data):
        '''Put data into the search tree.'''
	
        size = self.size + 1
	
        # if tree is empty
        if self.root is None:
            self.root = BSTNode(data)
            return
	
	
        # search for data and its would-be parent
        p, q = self.find_and_parent(data)
        if p is not None: 
            p.count += p.count 
            return

        # make data a child of q
        if data < q.data:
            assert q.left is None
            q.left = BSTNode(data)
        else:
            assert q.right is None
            q.right = BSTNode(data)

    def find(self, data):
        '''Find data, return None if data is not present.'''
        p, _ = self.find_and_parent(data)
        if p is None: return None
        else: return p.data


    def find_and_parent(self, data):
        '''Search for data, returning the node containing data and its parent.
        If data doesn't exist, we return None and data's would-be parent.'''
        q = None           # parent
        p = self.root      # current node
        while p is not None and p.data != data:
            q = p
            if data < p.data:
                p = p.left
            else:
                p = p.right
        return p, q

    def majority_element(self, root):
	'''Recursively build the inorder list.'''
        if root is not None:
            self.majority_element(root.left)
            if root.count > self.size // 2:
                return root.data
            self.majority_element(root.right)

bst = BinarySearchTree()

bst.insert(3)
bst.insert(3)
bst.insert(5)
bst.insert(2)
bst.insert(5)
bst.insert(5)
bst.insert(2)
bst.insert(5)
bst.insert(5)

print bst.majority_element(bst.root), "is the majority element."
