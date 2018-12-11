import math

def nextMove(n, r, c, grid):
    prinX = prinY = 0 
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p': #Princess's position
                prinX = i
                prinY = j 
                break

    angle = math.atan2(prinX-r, c-prinY)
    b = angle/math.pi*180
    if b > 0 and b < 180:
        return "DOWN"
    elif b > -180 and b < 0:
        return "UP"
    elif b == 0:
        return "LEFT"
    else:
        return "RIGHT"


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
