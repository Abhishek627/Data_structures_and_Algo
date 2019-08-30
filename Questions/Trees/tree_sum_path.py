'''
Maximum path sum in a tree between any 2 nodes --- MaxSumPathAny
Maximum path sum in a tree between 2 leaves --- MaxSumPathLeaves
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def MaxSumPathAny(root):
    '''
    There are 4 options at every node for making it max sum path
        a. through that node
        b. Node+left
        c. Node+right
        d. Node+ left+right
    :param root:
    :return:
    '''

    if not root:
        return 0

    sum_left = MaxSumPathAny(root.left)
    sum_right = MaxSumPathAny(root.right)

    sum_max_single_child = max(max(sum_left, sum_right) + root.data, root.data)
    sum_max_node = max(sum_max_single_child, sum_left + sum_right + root.data)
    MaxSumPathAny.res = max(MaxSumPathAny.res, sum_max_node)
    return sum_max_single_child  # Making sure function return sum of only 1 side


def MaxSumPathLeaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return root.data

    sum_left = MaxSumPathLeaves(root.left)
    sum_right = MaxSumPathLeaves(root.right)

    if root.left and root.right:
        MaxSumPathLeaves.res = max(MaxSumPathLeaves.res, sum_left + sum_right + root.data)
        return max(sum_right, sum_right) + root.data

    if root.left:
        return sum_left + root.data
    if root.right:
        return sum_right + root.data


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(3)

    MaxSumPathAny.res = float("-inf")
    MaxSumPathAny(root)
    print MaxSumPathAny.res

    # MaxSumPathLeaves.res = float("-inf")
    # MaxSumPathLeaves(root)
    # print MaxSumPathLeaves.res

    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)
    MaxSumPathLeaves.res = float("-inf")
    MaxSumPathLeaves(root)
    print MaxSumPathLeaves.res
