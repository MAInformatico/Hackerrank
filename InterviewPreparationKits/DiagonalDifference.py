#!/bin/python3

import os
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    firstDiagonal = [arr[i][i] for i in range(len(arr))]
    
    secondDiagonal = [arr[i][~i] for i in range(len(arr))]
    
    return abs(sum(firstDiagonal) - sum(secondDiagonal))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
