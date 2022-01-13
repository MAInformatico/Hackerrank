class TDAQueue(object):
    def __init__(self):
        self.values = []
    
    def show(self):
        i = self.values.pop()
        self.values.append(i)
        return i

    def pop(self):
        return self.values.pop()
    
    def include(self, value):
        self.values.insert(0,line)
        


numQueries = int(input())
data = TDAQueue()

for i in range(numQueries):
    line = map(int, input().split())
    line = list(line)
    if line[0] == 1:
        data.include(line[1])
    elif line[0] == 2:
        data.pop()
    else:
        v = str(data.show())
        result = v.split(',')
        print(result[1][1:-1])
