#!/bin/python3

import os
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):    
    open_brackets, closed_brackets = ['(', '{', '['], [')', '}', ']']
    matchs = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            if len(stack) == 0:
                return "NO"
            if stack[-1] == matchs[i]:
                stack.pop()
            else:
                return "NO"
    
    if len(stack) == 0:
        return "YES"    
    return "NO"
        
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
