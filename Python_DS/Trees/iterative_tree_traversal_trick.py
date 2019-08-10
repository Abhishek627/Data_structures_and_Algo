'''
Morris traversal trick to do any tree traversal iteratively instead of doing it using stacks.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def iterative_morris_inorder(root):
    from collections import defaultdict
    count_dict = defaultdict(int)
    stack = []
    if not root:
        return stack
    stack.append(root)
    while stack:
        curr = stack[-1]
        if not curr:
            stack.pop()
            continue

        count = count_dict[curr]
        if count == 0:
            stack.append(curr.left)
        elif count == 1:
            print curr.val,
        elif count == 2:
            stack.append(curr.right)
        else:
            stack.pop()
        count_dict[curr] += 1


def iterative_morris_preorder(root):
    from collections import defaultdict
    count_dict = defaultdict(int)
    stack = []
    if not root:
        return stack
    stack.append(root)
    while stack:
        curr = stack[-1]
        if not curr:
            stack.pop()
            continue

        count = count_dict[curr]
        if count == 0:
            print curr.val,
        elif count == 1:
            stack.append(curr.left)
        elif count == 2:
            stack.append(curr.right)
        else:
            stack.pop()
        count_dict[curr] += 1


def iterative_morris_postorder(root):
    from collections import defaultdict
    count_dict = defaultdict(int)
    stack = []
    if not root:
        return stack
    stack.append(root)
    while stack:
        curr = stack[-1]
        if not curr:
            stack.pop()
            continue

        count = count_dict[curr]
        if count == 0:
            stack.append(curr.left)
        elif count == 1:
            stack.append(curr.right)
        elif count == 2:
            print curr.val,
        else:
            stack.pop()
        count_dict[curr] += 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    iterative_morris_inorder(root)
    print "\n"

    iterative_morris_preorder(root)
    print "\n"

    iterative_morris_postorder(root)
