# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node(object):
    __slots__ = ['children', 'is_last']

    def __init__(self):
        self.children = [None] * 10
        self.is_last = 0


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add_entries(self, val):
        if not val:
            return 1
        curr = self.root
        for i in val:
            idx = ord(i) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            if curr.is_last:
                return 1
        curr.is_last = 1
        for child in curr.children:
            if child:
                return 1
        return 0


def prefix_sets(queries):
    t = Trie()
    for q in queries:
        if t.add_entries(q):
            print "BAD SET"
            print q
            return
    print "GOOD SET"


if __name__ == '__main__':
    q = int(raw_input())
    queries = []
    for i in range(q):
        queries.append(raw_input().strip())

    prefix_sets(queries)



