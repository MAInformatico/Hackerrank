#!/bin/python3

import os
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    result = 'NO'
    
    for i in range(len(s)):
        firstDigit = int(s[ : i + 1])
        auxS = str(firstDigit)
        
        if len(auxS) != len(s):
            currentDigit = firstDigit
            while len(auxS) < len(s):
                currentDigit += 1
                auxS += str(currentDigit)
                
                if auxS == s:
                    result = f"YES {firstDigit}"
                    break
    print(result)
    
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
