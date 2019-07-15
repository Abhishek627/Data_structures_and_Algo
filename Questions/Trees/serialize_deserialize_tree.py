'''
It basically means flatten the structure to some format which can be transmitted over network
and reconstructed later on, i.e, serialize first and de-serialize later on

I'm going to convert a tree to it's preorder form as it resembles how we approach the serialization issue,
deal with root first and then left child followed by right child
'''

from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def preorder_traversal(root):
    if root:
        print root.val,
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def serialize_tree(root):
    if not root:
        return 'X,'
    return str(root.val) + "," + serialize_tree(root.left) + serialize_tree(root.right)

def deserialize_tree(serialized_data):
    serial_arr= serialized_data.split(",")
    return deserialize_helper(deque(serial_arr))

def deserialize_helper(serial_queue):
    item = serial_queue.popleft()
    if item == "X":
        return None
    newNode= Node(int(item))
    newNode.left = deserialize_helper(serial_queue)
    newNode.right = deserialize_helper(serial_queue)
    return newNode

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # print serialize_tree(root)
    preorder_traversal(root)
    print "\n \n"
    preorder_traversal(deserialize_tree(serialize_tree(root)))