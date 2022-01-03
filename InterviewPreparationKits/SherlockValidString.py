#!/bin/python3

import os
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    arraySize = Counter(s)
    sCounter = Counter(arraySize.values())
          
    if len(sCounter) == 1:
        return "YES"

    if len(sCounter) > 2:
        return "NO"

    frecuencies = [ (i, j) for i, j in sorted(sCounter.items(), key=lambda x: x[1], reverse=True) ]

    if (frecuencies[0][0] == frecuencies[1][0] - 1 or frecuencies[1][0] == 1) and frecuencies[1][1] == 1:
        return "YES"
    else:
        return "NO"        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
