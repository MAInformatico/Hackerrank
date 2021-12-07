#!/bin/python3

import os
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def calculateSum(n):
    value = 0
    for i in list(n):
        value += int(i)
    return value

def superDigit(n, k):
    result=calculateSum(n)*k
    while result>9:
        currentValue = str(result)
        result = calculateSum(currentValue)
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
