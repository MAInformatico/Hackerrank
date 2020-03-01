import re

for _ in range(int(input())):
        data = input()
        data = re.sub(r" \&\&(?= )", " and", data)
        data = re.sub(r" \|\|(?= )", ' or', data)
        print(data)
