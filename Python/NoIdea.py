n, m = map(int,input().split())
data = input().split()
dataA = set(input().split())
dataB = set(input().split())
result = 0

for i in data:
    if i in dataA:
        result+=1
    if i in dataB:
        result-=1
print(result)
