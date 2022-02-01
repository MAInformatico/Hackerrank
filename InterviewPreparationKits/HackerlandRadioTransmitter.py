#!/bin/python3

import bisect #https://docs.python.org/3/library/bisect.html
import os
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    result = 0
    chunks = []
    x.sort()
    aux = [x[0]]
    for i in range(len(x) - 1):
        if x[i+1] - x[i] <= k: 
            aux.append(x[i+1])
        else:
            chunks.append(aux)
            aux = [x[i+1]]
    chunks.append(aux)
    
    for i in chunks:
        while i:
            leftIndex = bisect.bisect_right(i, i[0] + k, 0)-1
            rightIndex = bisect.bisect_right(i, i[leftIndex] + k, leftIndex + 1)
            i = i[rightIndex:]
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
