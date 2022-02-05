#!/bin/python3

import os
import sys

def arrayManipulation(n, queries):
    matrix = [0]*n
    for i, j, k in queries:
        for i in range(i-1, j):
            matrix[i] += k
    return max(matrix)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
