'''
Python 2.7 implementation fo trie data structures. Used for autocomplete,search and pattern matching

'''
class Node():
    def __init__(self):
        self.key=None
        self.value=None
        self.children= {}


class Trie():
    def __init__(self):
        self.root= Node() #Empty node as root

    def insert(self, word,value):
        curr_word=word
        curr_node=self.root
        while len(curr_word)>0:
            if curr_word[0] in curr_node.children:
                curr_node=curr_node.children[curr_word[0]]
            else:
                new_node= Node()
                new_node.key=curr_word[0]
                if len(curr_word)==1:
                    new_node.value=value
                curr_node.children[curr_word[0]]=new_node
                curr_node= new_node
            curr_word=curr_word[1:]

    def printAllNodes(self):
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            print nodes.pop(0).key


    def lookup(self,word):
        curr_word=word
        curr_node= self.root
        while len(curr_word)>0:
            if curr_word[0] in curr_node.children:
                curr_node=curr_node.children[curr_word[0]]
                curr_word = curr_word[1:]
            else:
                return "Not in trie yet"
        return curr_node.value

    def starts_with_prefix(self, prefix):
        '''
        Returns the list of all the words that start with that prefix
        :param prefix:
        :return:
        '''
        result=0
        curr_node= self.root
        for letter in prefix:
            if letter in curr_node.children:
                curr_node= curr_node.children[letter]
            else:
                return result
        # if curr_node == self.root:
        #     queue= [ node for key, node in curr_node.children.iteritems()]
        # else:
        queue= [curr_node]
        #Do a BFS
        while queue:
            curr_node= queue.pop()
            if curr_node.value:
                    result+=1
            queue= [node for key,node in curr_node.children.iteritems()]+queue
        return result


def makeTrie(words):
    trie = Trie()
    for word, value in words.items():
        trie.insert(word, value)
    return trie


if __name__ == '__main__':
    trie=makeTrie({'hello': 5, 'hat': 7, 'her': 1,'hell':4})
    trie.printAllNodes()
    print "hat lookup", trie.lookup('hat')
    print "hello lookup", trie.lookup('hello')
    print "her lookup",trie.lookup('her')
    print "hellos lookup",trie.lookup('hellos')
    print "hell lookup", trie.lookup('hell')
    print "HAT lookup", trie.lookup('HAT')

    print "Number of words with prefix h are", trie.starts_with_prefix('h')
    print "Number of words with prefix he are", trie.starts_with_prefix('he')