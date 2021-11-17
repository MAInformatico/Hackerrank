#!/bin/python3

import math
import os
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    result = {}
    
    for i in range(len(arr)):
        difference = abs(arr[i] - arr[i - 1])
        
        if difference not in result:
            result[difference] = [arr[i-1], arr[i]]
        else:
            result[difference].append(arr[i-1])
            result[difference].append(arr[i])
            
    keys = sorted(result.keys())
    return result[keys[0]]

    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
