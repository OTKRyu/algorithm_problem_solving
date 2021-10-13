import sys

input = sys.stdin.readline


def kruskal():
    global e
    cnt = 0
    idx = 0
    total = 0
    while cnt != e - 1:
        if union(es[idx][1], es[idx][2]):
            cnt += 1
            total += es[idx][0]
            idx += 1
        else:
            idx += 1
    return total


def find(x):
    while x != check[x]:
        x = check[x]
    return x


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return 0
    else:
        check[root_y] = root_x
        return 1


e = int(input())
v = [list(map(float, input().split())) for i in range(e)]
check = list(range(e))
es = []
for i in range(e):
    for j in range(i + 1, e):
        dis = ((v[i][0] - v[j][0]) ** 2 + (v[i][1] - v[j][1]) ** 2) ** (0.5)
        es.append([round(dis, 2), i, j])
es.sort(key=lambda x: x[0])
print(kruskal())
