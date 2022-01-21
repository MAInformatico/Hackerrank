def execute(op,value,text):
    op = int(op)
    if op in (1,2,3):
        value = value[0]
        if op in (2,3):
            value = int(value)
        
    if op == 1:
        text.append(text[-1] + value)
    elif op == 2:
        text.append(text[-1][:-value])
    elif op == 3:
        print(text[-1][value - 1])
    elif op == 4:
        text.pop()
        
Q = int(input())
stack = ['']
for _ in range(Q):
    operation, *value = input().split()
    execute(operation,value,stack)
