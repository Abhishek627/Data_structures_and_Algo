# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return symmetryHelper(root.left, root.right)


def symmetryHelper(rleft, rright):
    if not rleft and not rright:
        return True

    if rleft is None or rright is None:
        return False


    if rleft.val != rright.val:
        return False

    return symmetryHelper(rleft.left, rright.right) and symmetryHelper(rleft.right, rright.left)


if __name__ == '__main__':
    t= TreeNode(1)
    t.left = TreeNode(2)
    t.right= TreeNode(2)
    t.left.left= TreeNode(3)
    t.left.right= TreeNode(4)
    t.right.left= TreeNode(4)
    t.right.right = TreeNode(3)

    print Solution().isSymmetric(t)