while True:
    a, b,c=map(int, input().split())
    if (a,b,c) ==(0,0,0):
        break
    else:
        if a>b:
            a,b=b,a
        if b>c:
            b,c=c,b
        if a**2 +b**2 == c**2:
            print('right')
        else:
            print('wrong')