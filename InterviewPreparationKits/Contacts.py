#!/bin/python3

N = int(input())

dictData = {}

def addWord(dictData, word):
    
    if word == "":
        return
    
    if word[0] in dictData:
        dictData[word[0]]['count'] += 1
        
    else:
        dictData[word[0]] = { 'count': 1 }
        
    addWord(dictData[word[0]], word[1:])
    
def findWord(dictData, word):
    
    if word[0] not in dictData:
        return 0
    
    else:
        if len(word) == 1:
            return dictData[word[0]]['count']
        
        else:
            return findWord(dictData[word[0]], word[1:])

for i in range(N):
    line = input()
    query, word = line.split()
    if query == "add":
        addWord(dictData, word)
    elif query == "find":
        print(findWord(dictData, word))
    else:
        pass
