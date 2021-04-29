#!/bin/python3

import os
import random
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    subsequences = [0 for _ in s1]
    for i in s2:
        max_length = 0
        for j in range(len(s1)):
            aux = subsequences[j]
            if i == s1[j]:
                subsequences[j] = max_length + 1
            if subsequences[j] > 0 and aux > 0:
                max_length = max(aux, max_length)
    return max(subsequences)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
