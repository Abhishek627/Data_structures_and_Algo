'''
Basic Implementation of queues in python 2.7

Python supports creation of queues using lists but they are inefficient in removing and adding from start and end.
So we can use deque from collections to support our use case
__author__: Abhishek Sharma
'''

from collections import deque

class Inbuilt_Queue(object):

    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        # Should remove the first entry (from left) which came ,i.e, FIFO
        if len(self.queue) < 1:
            print "Queue is empty. Underflow error"
        else:
            return self.queue.popleft()

if __name__ == '__main__':
    q = Inbuilt_Queue()
    q.push("I")
    q.push("MADE")
    q.push("A")
    q.push("QUEUE")

    print list(q.queue)
    print q.pop()
