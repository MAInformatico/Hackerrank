#!/bin/python3

import os
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    specialCharacters = "!@#$%^&*()-+"
    
    checkNums = 1
    checkLower = 1
    checkUpper = 1
    checkSpecial = 1
    for i in password:
        if i.isdigit(): checkNums = 0
        elif i.islower(): checkLower = 0
        elif i.isupper(): checkUpper = 0
        elif i in specialCharacters: checkSpecial = 0
    return max(6-n, checkNums + checkLower + checkUpper + checkSpecial)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
