import heapq


def dijkstra(g, t):
    global n
    minimums = [100 * n] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, t))
    while heap:
        tmp = heapq.heappop(heap)
        if minimums[tmp[1]] > tmp[0]:
            minimums[tmp[1]] = tmp[0]
            for i in range(1, n + 1):
                if g[tmp[1]][i] != -1:
                    heapq.heappush(heap, (tmp[0] + g[tmp[1]][i], i))
        else:
            continue
    return minimums


for tc in range(int(input())):
    n, m, x = map(int, input().split())
    d_forth = [[-1 for j in range(n + 1)] for i in range(n + 1)]
    d_back = [[-1 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        s, e, w = map(int, input().split())
        d_forth[s][e] = w
        d_back[e][s] = w
    d_fs = dijkstra(d_forth, x)
    d_bs = dijkstra(d_back, x)
    maximum = 0
    for i in range(1, n + 1):
        if d_fs[i] + d_bs[i] > maximum:
            maximum = d_fs[i] + d_bs[i]
    print('#{} {}'.format(tc + 1, maximum))