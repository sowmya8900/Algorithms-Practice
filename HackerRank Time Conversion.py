'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen
'''

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
    # Write your code here
    l = list(map(str, s.split(':')))
    print(l)
    if(l[2][2]) == "P":
        if(l[0] != '12'):
            l[0] = int(l[0])
            l[0] += 12
        l[2] = l[2].replace("P", "")
    if(l[2][2]) == "A":
        if(l[0] == "12"):
            l[0] = l[0].replace("12", "00")
        l[2] = l[2].replace("A", "")
    l[2] = l[2].replace("M", "")
    l[0] = str(l[0])
    ans = ":".join(l)
    return(ans)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
