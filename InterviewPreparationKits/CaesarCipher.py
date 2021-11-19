#!/bin/python3

import os
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ''
    
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            result += chr((ord(i) - 65 + k) % 26 + 65)
        elif ord(i) >= 97 and ord(i) <= 122:
            result += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            result += i
            
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
