# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        return True


def main():
    root= TreeNode(18)
    root.left = TreeNode(8)
    root.right= TreeNode(20)
    root.right.left= TreeNode(10)
    root.right.right = TreeNode(30)
    ret = Solution().isValidBST(root)
    print ret

if __name__ == '__main__':
    main()