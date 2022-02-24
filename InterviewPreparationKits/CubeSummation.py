#!/bin/python3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N,M = [int(s) for s in input().split()]
        matrix = {}
        for j in range(M):
            request = input().split()
            if request[0] == "UPDATE":
                matrix[request[1]+" "+request[2]+" "+request[3]] = int(request[4])
            else:
                x1 = int(request[1])
                y1 = int(request[2])
                z1 = int(request[3])
                x2 = int(request[4])
                y2 = int(request[5])
                z2 = int(request[6])
                result = 0
                for k,l in matrix.items():
                    current = [int(s) for s in k.split()]
                    if current[0] <= x2 and x1 <= current[0] and current[1] <= y2 and y1 <= current[1] and current[2] <= z2 and z1 <= current[2]:
                        result += l
                print(result)
