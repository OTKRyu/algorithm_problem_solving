def kruskal(tree, n):
    cnt = 0
    idx = 0
    result = 0
    while cnt < n:
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
    v, e = map(int, input().split())
    tree = [list(map(int, input().split())) for i in range(e)]
    disjoints = list(range(v + 1))
    tree.sort(key=lambda x: x[2])
    result = kruskal(tree, v)
    print('#{} {}'.format(tc + 1, result))
