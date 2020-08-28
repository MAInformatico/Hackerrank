for t in range(int(input())):
    input()
    lCube = [int(i) for i in input().split()]
    min_list = lCube.index(min(lCube))
    left = lCube[:min_list]
    right = lCube[min_list+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
