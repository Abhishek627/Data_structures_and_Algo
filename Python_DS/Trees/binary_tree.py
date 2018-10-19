'''
Tree implementationin python 2.7 (Skeleton taken from udacity DSA course)
How? --- What does tree have as components essentially ?
a. A node (vertices)
b. Some connections b/w those nodes (edges)
'''


class Node(object):
    '''
    Class to represent an individual node. Instantiate a bunch of these and create links b/w them
    to create a binary tree
    '''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.inorder_search(self.root, find_val)

    def print_tree(self):
        print "INORDER", self.inorder_print(self.root, "")[:-1]
        print  "POSTORDER",self.postorder_print(self.root, "")[:-1]
        print  "PREORDER",self.preorder_print(self.root, "")[:-1]
        print "LEVEL ORDER", self.level_order_traversal(self.root,"")[:-1]



    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    # def inorder_search(self,start,find_val):
    #     if start.left:
    #         return self.inorder_search(start.left,find_val)
    #     if start and start.value == find_val:
    #         return True
    #     if start.right:
    #         return self.inorder_search(start.right,find_val)
    #     return False

    def inorder_search(self,start,find_vaL):
        if start:
            left= self.inorder_search(start.left,find_vaL)
            if start.value==find_vaL:
                return True
            right= self.inorder_search(start.right,find_vaL)
            if left or right:
                return True
        return False


    def preorder_print(self, start, traversal):
        '''

        :param start:
        :param traversal:
        :return:
        '''
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self,start,traversal):
        '''
        left-- root---right
        :param start:
        :param traversal:
        :return:
        '''
        if start:
            traversal= self.inorder_print(start.left,traversal)
            traversal+= (str(start.value)+"-")
            traversal= self.inorder_print(start.right,traversal)
        return  traversal

    def postorder_print(self,start,traversal):
        '''
        Left-- right --- root
        :param start:
        :param traversal:
        :return:
        '''
        if start:
            traversal= self.inorder_print(start.left,traversal)
            traversal= self.inorder_print(start.right,traversal)
            traversal+= (str(start.value)+"-")
        return  traversal

    def level_order_traversal(self,start,traversal):
        from collections import deque
        queue= deque()
        queue.append(start)
        while len(queue)>0:
            elem = queue.popleft()
            traversal+= str(elem.value)+ "-"
            if elem.left:
                queue.append(elem.left)
            if elem.right:
                queue.append(elem.right)
        return traversal

if __name__ == '__main__':

    # Set up tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    '''
                                        1
                                       / \
                                      2   3
                                     / \
                                    4   5
    '''
    # Should be True
    print tree.search(2)
    # Should be False
    print tree.search(6)

    for i in xrange(0,7):
        print i, tree.search(i)

    # Test print_tree
    # Should be 1-2-4-5-3
    tree.print_tree()
