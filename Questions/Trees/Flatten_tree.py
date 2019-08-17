'''
Flatten tree to a singly linked list

My approach would be to iterate through all the nodes recursively in either traversal mode and
set left to null while saving right value. And later appending that value to root.right (previously left value's end)
'''


# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :param root:
        :return:
        """
        if not root or (not root.left and not root.right):
            return None

        self.flatten(root.left)
        temp = root.right
        root.right = root.left
        root.left = None
        while root.right :
            root = root.right
        root.right = temp

        self.flatten(root.right)

    def flatten_smart(self, root):
        '''
        Found this solution in leetcode discuss.
        This is doing reverse postorder traversal
        '''
        if not root:
            return None

        self.flatten_smart(root.right)
        self.flatten_smart(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

    def iterative_traversal(self, root):
        if root:
            self.iterative_traversal(root.left)
            print root.val,
            self.iterative_traversal(root.right)

    def BinaryTreeToDLL(self, root):
        '''
        Converting a binary tree to a doubly linked list. (Simple DLL not a CDLL).
        I'll do it recursively finding righmost node in left subtree and making connection for it with root and finding leftmost
        node in right subtree and making connection to (root+left) subtree
        :param root:
        :return:
        '''
        if not root:
            return None

        root = self.BinaryTreeToDLLHelper(root)
        return root

    def BinaryTreeToDLLHelper(self, root):
        if not root:
            return None

        if root.left:
            left = self.BinaryTreeToDLL(root.left)

            while left.right:
                left = left.right

            left.right = root
            root.left = left

        if root.right:
            right = self.BinaryTreeToDLL(root.right)

            while right.left:
                right = right.left

            right.left = root
            root.right = right

        return root


def printDLL(root):
    if not root:
        return None

    while root:
        print root.val,
        root = root.right


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    Solution().flatten_smart(root)
    Solution().iterative_traversal(root)

    Solution().BinaryTreeToDLL(root)
    print "\n"
    printDLL(root)
