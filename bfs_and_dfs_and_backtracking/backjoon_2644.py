n = int(input())
tx, ty = map(int, input().split(' '))
m = int(input())
parents = {}
childs = {}
result = -1
check = [1 for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split(' '))
    parents[y] = x
    if childs.get(x):
        childs[x].append(y)
    else:
        childs[x] = [y]

def dfs(tx, cnt):
    global childs, parents, result, ty, check
    check[tx] = 0
    if tx == ty:
        result = cnt
        return 0
    flag = 1
    if childs.get(tx):
        for child in childs[tx]:
            if flag == 1 and check[child] == 1:
                flag = dfs(child, cnt+1)
    if parents.get(tx) and check[parents[tx]] == 1 and flag == 1:
        return dfs(parents[tx], cnt+1)
    return 1

dfs(tx, 0)
print(result)