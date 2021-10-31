#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives = 0
    zeros = 0
    negatives = 0
    for i in range(len(arr)):
        arr[i] = round(arr[i]/len(arr),6)
        if arr[i] > 0: positives += 1
        elif arr[i] == 0:
            zeros += 1
        else: negatives+=1
    print(positives/len(arr))
    print(negatives/len(arr))
    print(zeros/len(arr))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

