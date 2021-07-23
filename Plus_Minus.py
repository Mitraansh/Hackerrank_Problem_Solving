#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    countneg = 0
    count0 = 0
    countpos = 0
    n=len(arr)
    for i in range(n):
        if arr[i] < 0:
            countneg += 1
        if arr[i] > 0:
            countpos += 1
        if arr[i] == 0:
            count0 += 1
    print(f'{countpos/n:.6f}\n{countneg/n:.6f}\n{count0/n:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
