'''

https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''

# !/bin/python

from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    result = 0
    count2 = defaultdict(int)  #Keeps track of duplets
    count3 = defaultdict(int)  #Keeps track of triplets
    for val in arr:
        temp = val * r
        # Check if curr element makes a complete triplet
        result += count3[val]
        # Check if we can use curr element as a middle element
        count3[temp]+=count2[val]
        # Otherwise simply treat it as the first elem and update val*r by 1
        count2[temp] += 1

    return result

if __name__ == '__main__':
    # nr = raw_input().rstrip().split()
    #
    # n = int(nr[0])
    #
    # r = int(nr[1])
    #
    # arr = map(long, raw_input().rstrip().split())
    #
    # ans = countTriplets(arr, r)
    #
    # print ans

    print countTriplets([1, 5, 5, 25, 125], 5)
    inp = [1] * 100
    print countTriplets(inp, 1)

    print countTriplets([1, 2, 1, 2, 4], 2)
