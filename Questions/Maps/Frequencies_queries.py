#!/bin/python

import math
import os
import random
import re
import sys
from collections import defaultdict,Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    result=[]
    curr_dict= defaultdict(int)
    count = Counter()
    for idx,val in queries:
        if idx==1:
            # Insert entry in dict
            count[curr_dict[val]]-=1
            curr_dict[val]+=1
            count[curr_dict[val]]+=1

        elif idx==2:
            count[curr_dict[val]]-=1
            curr_dict[val]-=1 if curr_dict[val]>0 else 0
            count[curr_dict[val]]-=1

        else:
            result.append(1) if count[val] else result.append(0)

    return result


if __name__ == '__main__':

    q = int(raw_input().strip())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    ans = freqQuery(queries)
    print '\n'.join(map(str, ans))


