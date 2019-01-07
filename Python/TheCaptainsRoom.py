k = int(input())
arr = list(map(int, input().split()))
passengers = set(arr)
for x in passengers:
    count = 0
    for i in arr:
        if x == i:
            count += 1
            if count > 1:
                break
    if count == 1:
        print (x)
        break
