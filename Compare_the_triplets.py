#!/bin/python3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    x=[0,0]
    for i in range(len(a)):
        if (a[i]>b[i]):
            x[0]=x[0]+1
        elif(a[i]==b[i]):
            pass
        else:
            x[1]=x[1]+1
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
