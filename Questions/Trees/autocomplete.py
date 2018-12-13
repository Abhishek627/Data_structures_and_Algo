'''
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/


# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


class Node():
    def __init__(self):
        self.key = None
        self.value = None
        self.children = {}


class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word, value):
        curr_word = word
        curr_node = self.root
        while len(curr_word) > 0:
            if curr_word[0] in curr_node.children:
                curr_node = curr_node.children[curr_word[0]]
            else:
                new_node = Node()
                new_node.key = curr_word[0]
                curr_node.children[curr_word[0]] = new_node
                curr_node = new_node
            curr_word = curr_word[1:]
            if curr_node.value < value:
                curr_node.value = value

    def starts_with_prefix(self, prefix):
        curr_word = prefix
        curr_node = self.root
        while len(curr_word) > 0:
            if curr_word[0] in curr_node.children:
                curr_node = curr_node.children[curr_word[0]]
                curr_word = curr_word[1:]
            else:
                return -1
        return curr_node.value


def makeTrie(words):
    trie = Trie()
    for word, value in words.items():
        trie.insert(word, value)
    return trie


if __name__ == '__main__':
    trie = Trie()
    n, q = map(int, raw_input().strip().split(' '))
    for i in range(n):
        temp = raw_input().strip().split(' ')
        s, w = temp[0], int(temp[1])
        trie.insert(s, w)
    q_string = []
    for j in range(q):
        search = raw_input().strip()
        print(trie.starts_with_prefix(search))
