'''
Useful when we want to see if there is any order when things are dependent on each other.
There are 2-3 ways to do this:
1. BFS way
2. DFS way
'''

from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.vertices= vertices
        self.graph = defaultdict(list)

    def addEdge(self,start,end):
        self.graph[start].append(end)


    def topological_sort(self):
        visited = set()
        stack = []

        for i in xrange(self.vertices):
            if not i in visited:
                self.topological_sort_helper(i,visited,stack)
        stack.reverse()
        print stack

    def topological_sort_helper(self,start,visited,stack):
        visited.add(start)
        for neighbor in self.graph[start]:
            if not neighbor in visited:
                self.topological_sort_helper(neighbor,visited,stack)
        stack.append(start)

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)


    g.topological_sort()



