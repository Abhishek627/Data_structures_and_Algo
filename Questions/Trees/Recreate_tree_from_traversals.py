'''
Given 2 traversal of tree (inorder and pre,post, level). Recreate the tree.
Alternatively, verify if given traversals belong to the same tree.
'''


class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def recreate_tree(inorder, preorder, start, end):
    if start > end:
        return None
    root = BinaryTree(preorder[recreate_tree.preIndex])
    recreate_tree.preIndex += 1
    if start == end:
        return root

    index = inorder.index(root.val)
    root.left = recreate_tree(inorder, preorder, start, index - 1)
    root.right = recreate_tree(inorder, preorder, index + 1, end)
    return root


def recreate_tree_2(inorder, postorder, start, end):
    if start > end:
        return None
    root = BinaryTree(postorder[recreate_tree_2.postIndex])
    recreate_tree_2.postIndex -= 1
    if start == end:
        return root

    index = inorder.index(root.val)

    root.right = recreate_tree_2(inorder, postorder, index + 1, end)
    root.left = recreate_tree_2(inorder, postorder, start, index - 1)
    return root


def printInorder(root):
    if root:
        printInorder(root.left)
        print root.val,
        printInorder(root.right
                     )


if __name__ == '__main__':
    print "Construct a tree from pre and inorder traversal \n"
    recreate_tree.preIndex = 0
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    root = recreate_tree(inOrder, preOrder, 0, len(inOrder) - 1)
    printInorder(root)


    print "\n \nConstruct a tree from post and inorder traversal \n"
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    recreate_tree_2.postIndex= len(In)-1
    root = recreate_tree_2(In, post, 0, len(In) - 1)
    printInorder(root)