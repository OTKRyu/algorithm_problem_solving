def BFS(gs, queue, d, ep):
    possibles = []
    while queue:
        v = queue.pop(0)
        visited[v] = d
        if v == ep:
            return
        possibles = possibles + search(gs, v)
    if possibles:
        BFS(gs, possibles, d + 1,ep)
    else:
        return


def search(gs, v):
    ps = []
    for g in gs:
        if g[0] == v and not visited[g[1]]:
            ps.append(g[1])
    return ps


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    visited = [0] * (v + 1)
    gs = []
    tmps = []
    for i in range(e):
        tmp_s, tmp_e = map(int, input().split())
        tmps.append([tmp_s, tmp_e])
    for tmp in tmps:
        gs.append([tmp[1], tmp[0]])
    gs += tmps
    sp, ep = map(int, input().split())
    BFS(gs, [sp], 1, ep)
    if visited[ep] == 0:
        result = 0
    else:
        result = visited[ep] -1
    print('#{} {}'.format(tc, result))
