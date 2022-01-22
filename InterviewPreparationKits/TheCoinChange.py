#!/bin/python3

import os
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    #Let's use dynamic programming
    dynamicMatrix = [[0 for i in range(len(c)+1)] for j in range(n+1)]
    
    dynamicMatrix[0] = [1]*(len(c)+ 1)
    
    for i in range(1,n+1):        
        for j in range(1,len(c)+1):            
            if c[j-1] <= i:                
                dynamicMatrix[i][j] = dynamicMatrix[i-c[j-1]][j] + dynamicMatrix[i][j-1]                
            else:
                dynamicMatrix[i][j] = dynamicMatrix[i][j-1]
                    
    return dynamicMatrix[n][len(c)]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
