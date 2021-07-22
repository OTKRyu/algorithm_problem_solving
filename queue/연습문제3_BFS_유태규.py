def BFS(gs, v):
    result = []
    visited = [0] * 8
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        c = q.pop(0)
        result.append(c)
        adjs = []
        for g in gs:
            if g[0] == c and visited[g[1]] == 0:
                adjs.append(g[1])
        for adj in adjs:
            q.append(adj)
            visited[adj] = 1
    return result


gs = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]]
rgs = []
for g in gs:
    rgs.append([g[1],g[0]])
real_gs = gs + rgs

order = BFS(real_gs,1)
print(order)