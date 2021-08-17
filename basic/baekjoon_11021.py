tcs = int(input())
for tc in range(1, tcs+1):
    a, b = tuple(map(int, input().split()))
    print("Case #{}: {}".format(tc, a+b))