#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

def generateSubstrings(s):
    substr_list= []
    for i in xrange(len(s)):
        for j in xrange(i,len(s)):
            substr_list.append("".join(sorted(s[i:j+1])))
    return substr_list

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    result=0
    substrs= generateSubstrings(s)
    count_val= Counter(substrs).values()
    for val in count_val:
        if val>1:
            result+= val*(val-1)/2

    return result


if __name__ == '__main__':
    q = int(raw_input())
    for q_itr in xrange(q):
        s = raw_input()
        result = sherlockAndAnagrams(s)
    print result

    assert sherlockAndAnagrams('kkkk') == 10
    assert sherlockAndAnagrams('abcd') == 0
    assert sherlockAndAnagrams('abba') == 4