#!/bin/python3

import os
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#   

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    for i in range(0,len(sticks)-2):
        x = i
        y = i+1
        z = i+2
        if sticks[x] + sticks[y] > sticks[z]:
            if  sticks[x] + sticks[z] > sticks[y]:
                if sticks[y] + sticks[z] > sticks[x]:
                    return [sticks[z], sticks[y], sticks[x]]
    return [-1]
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
