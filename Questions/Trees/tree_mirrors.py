'''
Convert a tree to it's mirror and check if given trees are mirror of each other
'''

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


def convert_mirror(root):
    if not root:
        return None

    root.left,root.right= root.right, root.left
    convert_mirror(root.left)
    convert_mirror(root.right)


def check_mirror(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    return check_mirror(root1.left, root2.right) and check_mirror(root1.right,root2.left)






if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    preorder_traversal(root)
    convert_mirror(root)

    print "\n"
    preorder_traversal(root)

    print "\n\n"

    mirror_root = Node(1)
    mirror_root.left = Node(2)
    mirror_root.right = Node(3)
    mirror_root.left.left = Node(4)
    mirror_root.left.right = Node(5)
    print check_mirror(root,mirror_root)