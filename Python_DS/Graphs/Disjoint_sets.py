'''
Union-find data structure implementation.
Can be used in myriad of problems like:
1. Detecting cycles in undirected graph
2. Job-sequencing problems


'''

class DisjointSets():
    def __init__(self, input_list=[]):
        self.disjoint_set=[[x] for x in input_list]

    def find(self, item):
        for curr_set in self.disjoint_set:
            if item in curr_set:
                return self.disjoint_set.index(curr_set)
        return None

    def union(self,item1,item2):
        idx1= self.find(item1)
        idx2= self.find(item2)

        if idx1 is not None and idx2 is not None :
            if idx1 != idx2:
                self.disjoint_set[idx1]= self.disjoint_set[idx1]+ self.disjoint_set[idx2]
                del self.disjoint_set[idx2]
            else:
                print 'Cycle detected'



if __name__ == '__main__':
    ds= DisjointSets([1,2,3,4,5,6,7])
    ds.union(1,2)
    print ds.disjoint_set