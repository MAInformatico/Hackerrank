#!/bin/python3

import os
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()    
    countLetters = 0
    for i in string.ascii_lowercase:
        if i in s:
            countLetters += 1
    if countLetters == 26:
        return "pangram"
    else:
        return "not pangram"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
