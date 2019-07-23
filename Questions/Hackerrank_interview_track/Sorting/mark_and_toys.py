#!/bin/python

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    result = 0
    spent = 0
    prices.sort()
    for item in prices:
        if spent + item < k:
            spent += item
            result += 1

    return result


if __name__ == '__main__':
    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)

    print result
