# Queue.py

class Queue:    
    def __init__(self):
        '''create an empty FIFO queue'''
        self.queue = []

    def size(self):
        '''return number of items in the queue
        pre: none
        post: returns number of items in the queue'''
        return len(self.queue)

    def enqueue(self, data):
        '''insert data at end of queue
        pre: none
        post: data is added to the queue'''
        self.queue.append(data)

    def front(self):
        '''return first item in queue
        pre: queue is not empty; IndexError is raised if empty
        post: returns first item in the queue'''
        return self.queue[0]

    def dequeue(self):
        '''remove and return first item in queue
        pre: queue is not empty; IndexError is raised if empty
        post: removes and returns first item in the queue'''
        return self.queue.pop(0)
