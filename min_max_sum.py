#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    newarr=sorted(arr)
    minval=maxval=0
    for i in range(4):
        minval+=newarr[i]
    newarr1=newarr[::-1]
    for i in range(4):
        maxval+=newarr1[i]
    print (f'{minval} {maxval}')
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
