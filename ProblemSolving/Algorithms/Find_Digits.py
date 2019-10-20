#!/bin/python3

import os
import sys

# Complete the findDigits function below.
def findDigits(n):
    return sum([1 for i in str(n).replace('0','')if n%int(i)==0])
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
