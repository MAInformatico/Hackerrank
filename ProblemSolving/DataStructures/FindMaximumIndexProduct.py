#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    if len(arr)<=2:
        return 0
    lisIndex=[]
    for i in range(1,len(arr)-1):
        if arr[i-1]>arr[i] and arr[i]<arr[i+1]:
            lisIndex.append(i)
    if lisIndex:
        max_ind=max(lisIndex)
    else:
        return 0

    return (max_ind)*(max_ind+2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
