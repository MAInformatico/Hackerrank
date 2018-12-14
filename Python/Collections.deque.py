from collections import deque
data = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(data, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in data])
