#!/bin/python3

from collections import defaultdict
import os
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    dict1=defaultdict(list)
    dict2=defaultdict(list)
    localArray1=[item for item in arr]
    n=len(arr)
    for i in range(n):
        dict1[arr[i]].append(i)
        dict2[arr[i]].append(i)
    localArray2=sorted(arr)
    result1=0
    for i in range(n):
        if arr[i]!=localArray2[i]:
            dict1[arr[i]].append(dict1[localArray2[i]][0])
            dict1[arr[i]].pop(0)
            arr[dict1[localArray2[i]][0]],arr[i]=arr[i],arr[dict1[localArray2[i]][0]]
            dict1[localArray2[i]].pop(0)
            result1+=1
    
    result2=0
    localArray2=localArray2[::-1]
    for i in range(n):
        if localArray1[i]!=localArray2[i]:
            dict2[localArray1[i]].append(dict2[localArray2[i]][0])
            dict2[localArray1[i]].pop(0)
            localArray1[dict2[localArray2[i]][0]],localArray1[i]=localArray1[i],localArray1[dict2[localArray2[i]][0]]
            dict2[localArray2[i]].pop(0)
            result2+=1
    return min(result1,result2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
