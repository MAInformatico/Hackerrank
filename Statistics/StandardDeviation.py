n = int(input())
data = [int(x) for x in input().strip().split()]
print(round((sum([(x-(sum(data) / n))**2 for x in data])/n)**.5, 1))
