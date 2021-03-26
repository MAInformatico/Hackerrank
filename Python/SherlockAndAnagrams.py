#!/bin/python3

import os

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    dict={}
    result=0

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            aux= list(s[i:j].strip())
            aux.sort()
            check=''.join(aux)

            if check in dict: 
                result+=dict[check]
                dict[check]=dict[check]+1

            else: dict[check]=1       

    return result    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
