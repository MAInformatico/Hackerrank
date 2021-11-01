import re
while True:
    try:
        string = input().rstrip()    
        sc, mcv, content = string.split(";")
        if sc == "S":
            if mcv == "M":
                cap = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', content[:-2])
                result = " ".join(x.group(0).lower() for x in cap)
                print(result.rstrip())
                
            if mcv == "C":
                cap = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', content)
                result = " ".join(i.lower() for i in cap)
                print(result.rstrip())
                
            if mcv == "V":
                cap = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', content)
                result = " ".join(x.group(0).lower() for x in cap)
                print(result.rstrip())
                
        if sc == "C":
            if mcv == "M":
                lst = content.split(" ")
                res = []
                for i in range(len(lst)):
                    if i == 0:
                        res.append(lst[i].lower())
                    else:
                        res.append(lst[i].capitalize())
                result = "".join(i for i in res)
                result = result.rstrip() + "()"
                print(result.rstrip())
            if mcv == "C":
                lst = content.split(" ")
                result = "".join(i.capitalize() for i in lst)
                print(result.rstrip())
            if mcv == "V":
                lst = content.split(" ")
                res = []
                for i in range(len(lst)):
                    if i == 0:
                        res.append(lst[i].lower())
                    else:
                        res.append(lst[i].capitalize())
                result = "".join(i for i in res)
                print(result.rstrip())
            
    except EOFError:
        break
