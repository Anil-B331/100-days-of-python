def num(n):
    if(n==100):
        print(1)
        return
    
    print(n)
    num(n+1)

num(10)

