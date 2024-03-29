#!/bin/python3

import os
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    total = 0
    for i in s:
        total += i 

    allElementsAreOne = True if (total == len(s)) else False

    if allElementsAreOne :
        if len(s)%2 == 0:
            return "First"
        else:
            return "Second"
   
    else:
        xor = 0
        for val in s:
            xor = xor ^ val
        
        if(xor==0):
            return "Second";
        
        else:
            return "First";
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
