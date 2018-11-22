import re

for i in range(int(input())):
    result=True
    try:
        reg=re.compile(input())
    except re.error:
        result=False
    print(result)
