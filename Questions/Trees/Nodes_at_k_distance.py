'''
print all the nodes at k distance from the root.
Building on this, we can do print k distance node from any node.
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printKdistance(root, k):
    '''
    Iterative approach
    :param root:
    :param k:
    :return:
    '''
    import Queue
    q= Queue.Queue()
    q.put(root)
    result= []
    level= 1
    while not q.empty():
        root = q.get()
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)
        level-=1
        if level == 0:
            while not q.empty():
                temp = q.get()
                result.append(temp.data)
    return result

def printKdisRecur(root,k):
    if not root:
        return None
    if k==0:
        print root.data,
    printKdisRecur(root.left,k-1)
    printKdisRecur(root.right,k-1)



if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    t.right.right = Node(6)

    '''
             1
            /\ 
           2  3
          /\   \ 
         4  5   6
    '''

    print printKdistance(t,0) # result should be 4,5,6 because these are at a distance 2 from the node

    printKdisRecur(t,2)