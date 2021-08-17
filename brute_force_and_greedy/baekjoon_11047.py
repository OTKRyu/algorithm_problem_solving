import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))
coins.reverse()
cnt = 0
for coin in coins:
    if k//coin:
        cnt += k//coin
        k = k%coin
        if k ==0:
            break
print(cnt)