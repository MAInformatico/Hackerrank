#!/bin/python3

import os
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    dictionary = {"{" : "}" , "[" : "]", "(" : ")"}
    for i in s:
        if not stack:
            stack.append(i)
        elif i == dictionary.get(stack[-1]):
            stack.pop()            
        else:
            stack.append(i)
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
                                       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
