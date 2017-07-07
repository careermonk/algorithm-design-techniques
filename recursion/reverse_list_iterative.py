#Node of a Singly Linked List
class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    while head is not None:
        print "-->", head.data
        head = head.next

# iterative version
def reverse_list_iterative(head):
	prev = None
	current = head
	while(current is not None):
	    nextNode = current.next
	    current.next = prev
	    prev = current
	    current = nextNode
	
	head = prev
	return head
	
node1, node2, node3, node4, node5 = Node(1), Node(2), Node(3), Node(4), Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1
print_list(head)
head = node1
head = reverse_list_iterative(head)
print_list(head)
