class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print root.val,
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print root.val,
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print root.val,


def inorder_traversal_iterative(root):
    stack = []
    if not root:
        print ""
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print curr.val,
        curr = curr.right



def preorder_traversal_iterative(root):
    if not root:
        print ""
    stack = []
    curr = root
    stack.append(curr)
    while stack:
        curr = stack.pop()
        print curr.val,
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)



def postorder_traversal_iterative_2_stacks(root):
    '''
    This is bit different from other 2 traversals. Here if we look at the reverse of postorder, it looks like preorder
    except right is before left. So, we'll use this.
    '''
    stack_1 = []
    stack_2= []
    stack_1.append(root)
    while stack_1:
        curr = stack_1.pop()
        stack_2.append(curr.val)
        if curr.left:
            stack_1.append(curr.left)
        if curr.right:
            stack_1.append(curr.right)

    while stack_2:
        print stack_2.pop(),

def postorder_traversal_iterative_1_stacks(root):
    pass



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print "Inorder"
    inorder_traversal(root)
    print "\n Preorder"
    preorder_traversal(root)
    print "\n PostOrder"
    postorder_traversal(root)

    print "\n Inorder iterative"
    inorder_traversal_iterative(root)

    print "\n preorder iterative"
    preorder_traversal_iterative(root)

    print "\n Postorder iterative"
    postorder_traversal_iterative_2_stacks(root)

    print "\n postorder iterative with 1 stack"
    postorder_traversal_iterative_1_stacks(root)



