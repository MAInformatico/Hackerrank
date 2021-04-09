#!/bin/python3
from collections import Counter
import math
import os
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    aux = Counter(a)
    aux2 = Counter(b)
    aux.subtract(aux2)
    return sum(abs(i) for i in aux.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
