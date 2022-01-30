#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    valids = []
    area, i = 0, 0
    
    while i <= len(h):
        if not valids or (i < len(h) and h[i] > h[valids[-1]]):
            valids.append(i)
            i += 1
            
        else:
            last = valids.pop()
            if not valids:
                area = max(area, h[last] * i)
            else:
                area = max(area, h[last] * (i - valids[-1] - 1 ))
                
    return area
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
