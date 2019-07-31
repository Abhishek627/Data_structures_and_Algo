'''
Python implementation of BST. 
'''


class BinarySearchTree(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, new_val):
        if  new_val > self.value:
            #Go to right_child subtree
            if self.right_child:
                self.right_child.insert(new_val)
            else:
                self.right_child = BinarySearchTree(new_val)
        else:
            #Go to left subtree
            if self.left_child:
                self.left_child.insert(new_val)
            else:
                self.left_child= BinarySearchTree(new_val)

    def search(self, find_val):
        curr=self
        if curr.value< find_val  and curr.right_child:
            return curr.right_child.search(find_val)
        elif curr.value>find_val and curr.left_child:
            return curr.left_child.search(find_val)
        return curr.value== find_val

    def delete(self,del_val):
        '''
        Little tricky. Cqn divide it into 3 cases.If node to be deleted has :
        a. 2 children
        b. 1 children
        c. No children (Straight Forward)
        '''
    def print_tree(self):
        print "INORDER", self.inorder_print(self, "")[:-1]


    def inorder_print(self,start,traversal):
        '''
        left_child-- root---right_child
        :param start:
        :param traversal:
        :return:
        '''
        if start:
            traversal= self.inorder_print(start.left_child,traversal)
            traversal+= (str(start.value)+"-")
            traversal= self.inorder_print(start.right_child,traversal)
        return  traversal


if __name__ == '__main__':
    # Set up tree
    tree = BinarySearchTree(4)
    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    '''
                                        4
                                       / \
                                      2   5
                                     / \
                                    1   3
    '''

    tree.print_tree()

    # Check search
    # Should be True
    for i in xrange(0,10):
        print i,tree.search(i)