#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sums = []
    for i in arr:
        s = sum(arr) - i
        sums.append(s)
    print(min(sums), max(sums))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
