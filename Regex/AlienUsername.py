import re
for _ in range(int(input())):
    if(re.match(r'^[_\.][0-9]+[a-zA-Z]*_?$',input())):
        print('VALID')
    else:
        print('INVALID')
