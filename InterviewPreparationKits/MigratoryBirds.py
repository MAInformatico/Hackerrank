#!/bin/python3

import os
import random
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr = sorted(arr)
    dictFreq = {}
    result = 0
    counter = 0
    for i in arr:
        if i in dictFreq:
            dictFreq[i] += 1
        else:
            dictFreq[i] = 1
        if dictFreq[i] > counter:
            result = i
            counter = dictFreq[i]
    
    return result
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
