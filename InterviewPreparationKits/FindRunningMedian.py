from heapq import heappush,heappop

underHeap = []
upperHeap = []

N = int(input())

for _ in range(N):
    currentNumber = int(input())
    if (len(upperHeap) == 0):
        upperHeap.append(currentNumber)
        print(currentNumber)
        continue
    middleValue = upperHeap[0]
    if currentNumber >= middleValue:
        heappush(upperHeap,currentNumber)
    else:
        heappush(underHeap, -currentNumber)
    if len(underHeap) >= len(upperHeap):
        heappush(upperHeap, -heappop(underHeap))
    if len(upperHeap) >= len(underHeap) + 2:
        heappush(underHeap, -heappop(upperHeap))
    if (len(upperHeap) + len(underHeap)) % 2 == 1:
        print(float(upperHeap[0]))
    else:
        print((float(upperHeap[0]) + -underHeap[0]) / 2)
