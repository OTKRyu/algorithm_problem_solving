def topological_sort():
    q = []
    for i in range(1, v + 1):
        if ins[i] == 0:
            q.append(i)
    result = []
    while q:
        p = q.pop(0)
        result.append(p)
        for i in range(1, v + 1):
            if edges[p][i] == 1:
                ins[i] -= 1
                if ins[i] == 0:
                    q.append(i)
    return result

for tc in range(10):
    v, e = map(int, input().split())
    tmp = list(map(int, input().split()))
    edges = [[0 for j in range(v + 1)] for i in range(v + 1)]
    ins = [0 for i in range(v + 1)]
    for i in range(e):
        edges[tmp[i * 2]][tmp[i * 2 + 1]] = 1
    for i in range(1, v + 1):
        total = 0
        for j in range(1, v + 1):
            total += edges[j][i]
        ins[i] = total
    result = topological_sort()
    result = ' '.join(map(str, result))
    print('#{} {}'.format(tc + 1, result))

