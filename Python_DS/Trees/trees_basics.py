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
    stack_2 = []
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


def print_diameter(root, result):
    if not root:
        return 0

    left = print_diameter(root.left, result)
    right = print_diameter(root.right, result)

    result[0] = max(result[0], left + right)
    return max(left, right) + 1


def printPathRecur(root):
    '''
    Prints all the paths from root to all the leaf nodes
    :param root:
    :return:
    '''

    result = []
    printPathRecurHelper(root, result, 0)


def printPathRecurHelper(root, result, pathlen):
    if not root:
        return None

    if len(result) > pathlen:
        result[pathlen] = root.val
        del result[pathlen + 1:]  # or we can write a print function in below if to print only till pathLen instead of
        # complete result array
    else:
        result.append(root.val)
    if root.left is None and root.right is None:
        print result

    printPathRecurHelper(root.left, result, pathlen + 1)
    printPathRecurHelper(root.right, result, pathlen + 1)


def print_k_sum_path(root, k, sum_so_far, path):
    '''
    print all the paths with sum as K
    :param root:
    :param k:
    :return:
    '''
    if not root:
        return None

    path.append(root.val)
    sum_so_far+= root.val

    if k== sum_so_far:
        print "path is",path
    print_k_sum_path(root.left, k,sum_so_far, path)
    print_k_sum_path(root.right, k,sum_so_far, path)
    path.pop(-1)


if __name__ == '__main__':
    '''
                      1
                    /  \ 
                   2    3   
                  / \  / \ 
                 4  5  3  7
                           \ 
                            8      
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(3)
    root.right.right = Node(7)
    root.right.right.right = Node(8)

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

    result = [0]
    print_diameter(root, result)
    print "diameter of tree is", result[0]

    printPathRecur(root)


    path = []
    print_k_sum_path(root, 7, 0, path)
