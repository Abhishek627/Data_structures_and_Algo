'''


'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_paths(root,val,result):
    if not root:
        return None

    result.append(root.data)

    if root.data == val:
        return True

    left = print_paths(root.left,val,result)
    right= print_paths(root.right,val,result)

    if left or right:
        return True

    result.pop()
    return False




if __name__ == '__main__':
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)

    result=[]
    print_paths(root,0,result)
    print result