#!/bin/python3

import os
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    module = 10**9 + 7
    C1 = [0] * 26
    C2 = [0] * 26 * 26
    C3 = [0] * 26 * 26
    counter = 0
    alphabet = list(range(26))
    for i in s:
        c = ord(i) - 97
        p = 26 * c - 1
        q = c - 26
        for j in alphabet:
            q += 26
            p += 1
            counter += C3[q]
            C3[p] += C2[p]
            C2[p] += C1[j]
        C1[c] += 1

    result = counter%module
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
