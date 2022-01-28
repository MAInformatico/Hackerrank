import heapq # https://docs.python.org/3/library/heapq.html
result = []
isIncluded = set()

for _ in range(int(input())):
    command = list(map(int, input().split()))
    
    if command[0] == 1:
        heapq.heappush(result, command[1])
        isIncluded.add(command[1])
        
    elif command[0] == 2:
        isIncluded.discard(command[1])
        
    elif command[0] == 3:        
        while result[0] not in isIncluded:
            heapq.heappop(result)
            
        print(result[0])
