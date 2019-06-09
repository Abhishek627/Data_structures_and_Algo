#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    count = Counter(magazine)
    for word in note:
        if not word in count:
            return 'No'

        else:
            count[word] -= 1
    return 'Yes'


if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    print checkMagazine(magazine, note)


