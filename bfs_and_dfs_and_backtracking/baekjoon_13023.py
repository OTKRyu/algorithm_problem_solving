import sys

input = sys.stdin.readline

def dfs(step, c):
    if step == 5:
        return 1
    for i in range(len(adjs[c])):
        if check[adjs[c][i]] == 0:
            check[adjs[c][i]] = 1
            if dfs(step+1, adjs[c][i]):
                return 1
            else:
                check[adjs[c][i]] = 0
    else:
        return 0

n, m = map(int, input().split())
adjs = [[] for i in range(n)]
check = [0 for i in range(n)]
for i in range(m):
    f, b = map(int, input().split())
    adjs[f].append(b)
    adjs[b].append(f)

for i in range(n):
    if dfs(0,i):
        print(1)
        break
else:
    print(0)