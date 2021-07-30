#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    freq = {}
    counting = [freq.update({x: ar.count(x)}) for x in ar]
    pair_list = []
    for value in freq.values():
        pair_list.append(value)
    print(pair_list)
    pairs = 0
    for i in pair_list:
        if i == 2:
            pairs += 1
        else:
            pairs += i//2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
