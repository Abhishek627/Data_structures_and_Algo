'''
closestValue: prints the closest value in BST to the target value
bstRelative: prints inorder successor and ancestor to a given BST node
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def closestValue(root, target):
    result = [float("inf"), float("inf")]
    closeHelper(root, target, result)
    return result[1]


def closeHelper(root, target, result):
    if not root:
        return 0

    if abs(root.val - target) < result[0]:
        result[0] = abs(root.val - target)
        result[1] = root.val

    if target > root.val:
        closeHelper(root.right, target, result)
    else:
        closeHelper(root.left, target, result)


def KclosestValue(root, target, k):
    '''
    Above question can be modified to print k nearest values instead of a single value
    :param root:
    :param target:
    :return:
    '''


def bstRelative(root, key):
    if not root:
        return

    if root.val == key:
        # predecessor will be rightmost node in leftsubtree
        # successor will be leftmost node in rightsubtree
        if root.left:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            bstRelative.pre = tmp.val

        if root.right:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            bstRelative.suc = tmp.val
        return

    if root.val > key:
        bstRelative.pre = root.val
        bstRelative(root.left, key)
    else:
        bstRelative.suc = root.val
        bstRelative(root.right, key)


if __name__ == '__main__':
    t = TreeNode(9)
    t.left = TreeNode(4)
    t.right = TreeNode(17)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(6)
    t.left.right.left = TreeNode(5)
    t.left.right.right = TreeNode(7)
    t.right.right = TreeNode(22)
    t.right.right.left = TreeNode(20)

    print closestValue(t, 4)  # 4
    print closestValue(t, 18)  # 17
    print closestValue(t, 12)  # 9

    bstRelative.pre = None
    bstRelative.suc = None
    key = 22
    bstRelative(t, key)

    print bstRelative.pre, bstRelative.suc
