#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    g = []
    for i in grades:
        if i < 38 or i == 100:
            g.append(i)
        else:
            new_g = i
            temp = new_g % 10
            if temp < 5:
                new_g -= temp
                new_g += 5
            else:
                new_g -= temp
                new_g += 10 
            if (new_g - i) < 3:
                g.append(new_g)
                temp = 0
            else:
                g.append(i)
    return g

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
