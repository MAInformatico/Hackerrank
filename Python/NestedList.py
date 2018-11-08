if __name__ == '__main__':
    nestedList = []
    for _ in range(0,int(input())):
        name = input()
        score = float(input())
        nestedList.append([name, score])
        
second_highest = sorted(list(set([marks for name, marks in nestedList])))[1]
print('\n'.join([a for a,b in sorted(nestedList) if b == second_highest]))
