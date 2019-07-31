#!/bin/python


import os


class Node(object):
    def __init__(self, value):
        self.data = value
        self.children = [None] * 26
        self.matches = 0


class Trie(object):
    def __init__(self):
        self.root = Node("")

    def add_entries(self, val):
        if not val:
            return None
        curr = self.root
        for i in val:
            idx = ord(i) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Node(i)
            curr.children[idx].matches += 1
            curr = curr.children[idx]

    def find_entries(self, val):
        curr = self.root
        for i in val:
            idx = ord(i) - ord('a')
            curr = curr.children[idx]
            if not curr:
                return 0

        if not curr:
            return 0
        return curr.matches


def contacts(queries):
    t = Trie()
    result=[]
    for q in queries:
        if q[0] == "add":
            # Add entries to the trie
            t.add_entries(q[1])
        if q[0] == "find":
            # search trie for number of results
            result.append(t.find_entries(q[1]))

    return result


if __name__ == '__main__':
    fptr = open('contacts_input.txt', 'w')

    queries_rows = int(raw_input())

    queries = []

    for _ in xrange(queries_rows):
        queries.append(raw_input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
