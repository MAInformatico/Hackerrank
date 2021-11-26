#!/bin/python3

import os
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    result=[[] for _ in range(len(arr))]
    for i,j in enumerate(arr):
        key,value=j
        if i<len(arr)//2:
            value='-'
        result[int(key)].append(value)
    print(( ' '.join([' '.join(i) for i in result])).strip())

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
