#!/bin/python3

import math

t = int(input())
for i in range(t):
    result = 1
    localSumB = 0
    n = int(input())
    b = input()
    for i in b.split():
        i=int(i)
        localSumB += i
        result *= pow(i,(i-1))
        result = result % 1000000007


    result *= pow(localSumB,(n-2))
    result = int(result % 1000000007)
    print (result)
