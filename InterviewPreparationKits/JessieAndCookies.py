#!/bin/python3

import os
import sys
import heapq #https://docs.python.org/3/library/heapq.html

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):    
    heapq.heapify(A)
    result = 0 
    while True:
        if len(A) == 1 and A[0] < k:
            return -1
        
        if A[0] >= k:
            return result
        else:
            minimum = heapq.heappop(A)
            secondMin = heapq.heappop(A)
            newValue = minimum + 2*secondMin
            result += 1
            heapq.heappush(A, newValue)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
