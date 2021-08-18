a, b = 1, 1
while (a, b) != (0, 0):
    a, b = tuple(map(int, input().split()))
    if (a,b) != (0, 0):
        print(a+b)