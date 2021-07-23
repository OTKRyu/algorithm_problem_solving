def BFS(g, s):
    queue = []
    queue.append(s)
    cnt_r = 1
    while queue:
        v = queue.pop(0)
        ps = search_r(g, v)
        if ps:
            queue.append(ps)
            cnt_r += 1
    queue = []
    queue.append(s)
    cnt_d = 1
    while queue:
        v = queue.pop(0)
        ps = search_d(g, v)
        if ps:
            queue.append(ps)
            cnt_d += 1
        else:
            break
    return [cnt_d, cnt_r, cnt_r * cnt_d]


def search_r(g, v):
    if 0 <= v[1] + 1 < n and g[v[0]][v[1] + 1] != 0:
        return [v[0], v[1] + 1]
    else:
        return None


def search_d(g, v):
    if 0 <= v[0] + 1 < n and g[v[0] + 1][v[1]] != 0:
        return [v[0] + 1, v[1]]
    else:
        return None


for tc in range(1, int(input()) + 1):
    n = int(input())
    large_matrix = []
    results = []
    for i in range(n):
        large_matrix.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if large_matrix[i][j] != 0:
                if i == 0 and j == 0:
                    results.append(BFS(large_matrix, [i, j]))
                elif i == 0 and large_matrix[i][j - 1] == 0:
                    results.append(BFS(large_matrix, [i, j]))
                elif j == 0 and large_matrix[i - 1][j] == 0:
                    results.append(BFS(large_matrix, [i, j]))
                else:
                    if large_matrix[i][j - 1] == 0 and large_matrix[i - 1][j] == 0:
                        results.append(BFS(large_matrix, [i, j]))
    results.sort(key=lambda x:(x[2],x[0]))
    print('#{} {}'.format(tc, len(results)), end=' ')
    for result in results:
        print('{} {}'.format(result[0], result[1]), end=' ')
    print()
