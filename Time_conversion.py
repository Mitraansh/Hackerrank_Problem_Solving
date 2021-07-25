#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    news = ''
    if s[8:] == 'AM':
        if int(s[:2]) == 12:
            news = f'00{s[2:8]}'
        else:
            news = s[:8]
    else:
        if int(s[:2]) != 12:
            a = int(s[:2]) + 12
            news = f'{a}{s[2:8]}'
        else:
            news = s[:8]

    return news

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
