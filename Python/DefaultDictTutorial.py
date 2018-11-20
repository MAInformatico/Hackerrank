from collections import defaultdict

x, y = map(int, input().split())
d = defaultdict(lambda: -1)

for i in range(1, x+1): 
    word = input()
    d[word] = d[word] + ' ' + str(i) if word in d else str(i)

for _ in range(y):
    print(d[input()])
