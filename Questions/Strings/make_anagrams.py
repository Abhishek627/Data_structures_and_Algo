#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter,OrderedDict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    result= 0
    result_a= set(list(a))
    result_b= set(list(b))
    common= result_a.intersection(result_b)
    different= result_a.symmetric_difference(result_b)
    for item in different:
        result+= a.count(item)+b.count(item)
    for item in common:
        result+= abs(a.count(item)-b.count(item))
    return result

if __name__ == '__main__':
    a= "cde"
    b= "abc"
    a="fcrxzwscanmligyxyvym"
    b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"
    print OrderedDict(Counter(a))
    print OrderedDict(Counter(b))
    print makeAnagram(a,b)