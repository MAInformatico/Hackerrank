import re

ipv4=r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$'
ipv6=r'^(([\d|a-f]|){4}\:){7}[\d|a-f|]{4}$'

for _ in range(int(input())):
    data=input()
    
    if re.match(ipv4,data):
        print('IPv4')
    elif re.match(ipv6,data):
        print('IPv6')
    else:
        print('Neither')
