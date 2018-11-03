'''
Python implementation of segment tree. Used to range queries like min/max/sum of array items in a given range
Will have 3 main methods,
1, build---   build a segment tree from the given array
2. Update---  update the value of a certain array element
3. Query---   Queries whatever we buld the segtree for (Internal nodes should contain  data suitable for this)

This DS is good when we have large num of queries, otherwise we can simply use normal array ops as they would give
O(1) update.

Given code is for min elem, https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/
Read this solution too :
https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/python-well-commented-solution-using-segment-trees
(Uses node instead of array to eliminate the problem of large empty array)
'''


class Segment_Tree():
    def __init__(self, A):
        self.A = A
        self.tree = [None] * 2 * len(self.A)  # check how to good correct size, so as to not waste extra space

    def build(self, node, start, end):
        if (start == end):
            self.tree[node] = self.A[start]
        else:
            mid = (start + end) / 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, start, end, idx, value):
        if start == end:
            self.A[idx] = value
            self.tree[node] = value
        else:
            mid = (start + end) / 2
            if start <= idx <= mid:
                # look in left subtree
                self.update(2 * node, start, mid, idx, value)
            else:
                self.update(2 * node + 1, mid + 1, end, idx, value)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if (r < start or end < l):
            return 100005
        if (l <= start and end <= r):
            return self.tree[node]
        mid = (start + end) / 2

        left_val = self.query(2 * node, start, mid, l, r)
        right_val = self.query(2 * node + 1, mid + 1, end, l, r)
        return min(left_val, right_val)


# ToDo: Lazy propogation (Update a node and mark it's children as to be updated . Update them only in case of new update or query)


if __name__ == '__main__':
    N, Q = map(int, raw_input().strip().split(' '))
    A = map(int, raw_input().split(' '))
    seg_tree = Segment_Tree(A)
    seg_tree.build(1, 0, N - 1)
    print seg_tree.tree
    for i in range(Q):
        op = raw_input().strip().split(' ')
        if op[0] == 'u':
            idx = int(op[1]) - 1
            value = int(op[2])
            seg_tree.update(1, 0, N - 1, idx, value)
        else:
            l = int(op[1]) - 1
            r = int(op[2]) - 1
            print seg_tree.query(1, 0, N - 1, l, r)
