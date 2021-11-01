'''
Problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    f = {}
    for i in arr:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    print(f)
    a = list(f.values())
    print(a)
    a.remove(max(a))
    return(sum(a))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
