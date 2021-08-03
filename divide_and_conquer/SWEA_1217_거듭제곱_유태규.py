def power(n,m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return power(n,m//2)*power(n,m-m//2)

for _ in range(1, 11):
    tc = int(input())
    n, m = map(int, input().split())
    print('#{} {}'.format(tc, power(n,m)))