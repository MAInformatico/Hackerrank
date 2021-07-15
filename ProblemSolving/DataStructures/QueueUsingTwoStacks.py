from collections import deque

totalTest = int(input())
queue = deque()

for _ in range(totalTest):
    q = input().split()
    
    if q[0] == '1':
        queue.appendleft(int(q[1]))
    
    if q[0] == '2':
        queue.pop()
    
    if q[0] == '3':
        print(queue[-1])
