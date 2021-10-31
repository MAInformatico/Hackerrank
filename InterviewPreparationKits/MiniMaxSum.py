#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minimum , maximum = 0 , 0
    i = 0
    while i < len(arr) - 1:           
        minimum += arr[i]
        i+=1
    i = 1
    while i < len(arr):        
        maximum += arr[i]
        i+=1
    print(minimum,maximum)
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
