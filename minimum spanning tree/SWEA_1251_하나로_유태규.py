def kruskal(tree, n):
    cnt = 0
    idx = 0
    result = 0
    while cnt != n-1:
        c = tree[idx]
        if find(c[0]) == find(c[1]):
            idx += 1
        else:
            result += c[2]
            union(c[0], c[1])
            idx += 1
            cnt += 1
    return result


def union(x, y):
    disjoints[find(y)] = find(x)


def find(x):
    if x == disjoints[x]:
        return x
    else:
        return find(disjoints[x])

for tc in range(int(input())):
    v = int(input())
    islands_x = list(map(int, input().split()))
    islands_y = list(map(int, input().split()))
    e = float(input())
    tree = []
    for i in range(v):
        for j in range(i + 1, v):
            cost = ((islands_x[i] - islands_x[j]) ** 2 + (islands_y[i] - islands_y[j]) ** 2) * e
            tree.append([i, j, cost])
    disjoints = list(range(v))
    tree.sort(key=lambda x: x[2])
    result = int(round(kruskal(tree, v),0))
    print('#{} {}'.format(tc + 1, result))