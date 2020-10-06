from itertools import combinations

_,s,n = input(),input().split(),int(input())
a = list(combinations(s,n))
c = [i for i in a if 'a' in i]
print(len(c)/len(a))
