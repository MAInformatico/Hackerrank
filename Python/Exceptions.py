for i in range(int(input())):
    try:
        first,second=map(int,input().split())
        print(first//second)
    except Exception as e:
        print("Error Code:",e)        
