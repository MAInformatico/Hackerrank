def getKey(char):
    if char.islower():
        return(1,char)
    elif char.isupper():
        return(2,char)
    elif char.isdigit() :
        if int(char)%2==1:
            return(3,char)
        else :
            return(4,char)

print(*sorted(input(),key=getKey),sep='')
