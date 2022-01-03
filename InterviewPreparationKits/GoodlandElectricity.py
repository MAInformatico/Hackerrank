#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):    
    n=len(arr)
    aux=[]
    for i in range(n):
        if arr[i] == 1:
           aux.append(i) 
    finish = -1
    result = 0
    begin = 0
    while finish<n-1:
        i = bisect.bisect_right(aux,finish+k,begin)-1
        if i<0:
            return -1
        begin = i
        result += 1
        localFinish = aux[i]+(k-1)
        if localFinish == finish:
            return -1
        finish = localFinish
        
    return result
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
