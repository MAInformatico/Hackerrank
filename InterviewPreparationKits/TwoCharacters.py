#!/bin/python3

import os
import re
from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    result = 0
    for i in (combinations(set(s),2)):
        j = "".join(i)
        regexp = re.sub("[^%s]"%j, "",s)
        if len(regexp) > result and not re.search(r"(\w)\1", regexp) :
            result = len(regexp)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
