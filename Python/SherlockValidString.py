#!/bin/python3

import os

# Complete the isValid function below.
def isValid(s):    
    frequencyLetter = [s.count(letter) for letter in set(s) ]
    if max(frequencyLetter)-min(frequencyLetter) == 0:
        return 'YES'    
    elif frequencyLetter.count(max(frequencyLetter)) == 1 and max(frequencyLetter) - min(frequencyLetter) == 1:
        return 'YES'
    elif frequencyLetter.count(min(frequencyLetter)) == 1:
        frequencyLetter.remove(min(frequencyLetter))
        if max(frequencyLetter)-min(frequencyLetter) == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
