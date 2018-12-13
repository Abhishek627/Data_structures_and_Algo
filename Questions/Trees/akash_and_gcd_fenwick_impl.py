'''
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/akash-and-gcd-1-15/
'''


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def F(val):
    sum=0
    for i in xrange(1,val+1):
        sum+= gcd(i,val)
    return sum


class FenwickTree():
    def __init__(self,input_arr=[]):
        self.size= len(input_arr)
        self.BIT= [0]*len(input_arr)
        for i in range(1,self.size+1):
            self.update(i,input_arr[i-1])

    def update(self,idx,val, flag=0):
        while idx <= self.size:
            if flag:
                self.BIT[idx-1]+= val
            else:
                self.BIT[idx - 1] += F(val)
            idx += idx & (-idx)

    def query(self,x):
        sum=0
        while x>0:
            sum+=self.BIT[x-1]
            x-= x& (-x)
        return sum

    def compute(self,start,end):
        return self.query(end)-self.query(start-1)

if __name__ == '__main__':
    N= int(raw_input())
    input_arr= map(int,raw_input().strip().split(' '))
    print type(input_arr)
    ft = FenwickTree(input_arr)
    Q= int(raw_input())
    for i in xrange(Q):
        query= raw_input().split(' ')
        if query[0]=='C':
            print ft.compute(int(query[1]),int(query[2]))
        else:
            idx=int(query[1])
            val= F(int(query[2])) - F(input_arr[idx-1])
            ft.update(idx,val, flag=1)
