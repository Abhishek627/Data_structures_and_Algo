'''
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/
Simpler to implement than the segment tree. Can be used in suffix sum queries.
'''

class FenwickTree():
    def __init__(self,input_arr=[]):
        self.size= len(input_arr)
        self.BIT= [0]*len(input_arr)
        for i in range(1,self.size+1):
            self.update(i,input_arr[i-1])

    def update(self,idx,val):
        while idx <= self.size:
            self.BIT[idx-1]+= val
            idx += idx & (-idx)

    def query(self,x):
        sum=0
        while x>0:
            sum+=self.BIT[x-1]
            x-= x& (-x)
        return sum


if __name__ == '__main__':
    ft = FenwickTree([3,2,-1,6,5,4,-3,3,7,2])
    for i in xrange(1,11):
        print ft.query(i)