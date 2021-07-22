def union(x, y):
    ns[find(y)] = find(x)


def find(x):
    if x == ns[x]:
        return x
    else:
        return find(ns[x])


for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    ns = list(range(n + 1))
    for i in range(m):
        union(tmp[i * 2], tmp[i * 2 + 1])
    result = set()
    for i in range(n + 1):
        result.add(find(i))
    print('#{} {}'.format(tc, len(list(result)) - 1))
