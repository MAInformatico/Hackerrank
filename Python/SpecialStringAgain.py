#!/bin/python3

import math
import os
import random
from re import findall
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    result = n
    for i in range(n): 
        j = i
        while j < n - 1:
            j += 1
            if s[i] == s[j]:
                result += 1
            else:
                if s[i:j] == s[j+1:2*j-i+1]:
                    result += 1
                break
    return result
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
