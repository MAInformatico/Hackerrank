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
    stack=[]
    result=0
    i=0
    while i<len(h):
        
        if not stack or h[stack[-1]]<=h[i]:
            stack.append(i)
            i+=1
           
        else:
            top=stack.pop()
            result=max(result,h[top]*(i-stack[-1]-1 if stack else i))
    
    while stack:
        top=stack.pop()
        result=max(result,h[top]*(i-stack[-1]-1 if stack else i))
        
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
