'''
Lowest node from which both the target values can be reached.
Algo: recursion to check if value is present in left or right subtree
        and decide LCA on basis of that
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def LCA(root, x, y):
    if root == None:
        return None

    if (root.val == x or root.val == y):
        return root

    searchLeft = LCA(root.left, x, y)
    searchRight = LCA(root.right, x, y)

    if searchLeft and searchRight:
        return root

    if not searchRight and not searchLeft:
        return None

    return searchRight if searchRight else searchLeft


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print LCA(root, 2, 4).val
    print LCA(root, 4, 5).val
    print LCA(root, 2, 3).val
    print LCA(root, 1, 5).val
