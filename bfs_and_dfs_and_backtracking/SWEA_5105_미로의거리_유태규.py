def BFS(g, queue, d):
    possibles = []
    while queue:
        v = queue.pop(0)
        visited[v[0]][v[1]] = d
        possibles = possibles + search(g, v)
    if possibles:
        BFS(g, possibles, d + 1)
    else:
        return


def search(g, v):
    ps = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= v[0] + dy[i] < n and 0 <= v[1] + dx[i] < n and g[v[0] + dy[i]][v[1] + dx[i]] in [0, 3] and \
                visited[v[0] + dy[i]][v[1] + dx[i]] == 0:
            ps.append([v[0] + dy[i], v[1] + dx[i]])
    return ps


for tc in range(1, int(input()) + 1):
    n = int(input())
    visited = [[0 for i in range(n)] for j in range(n)]
    maze = []
    for i in range(n):
        maze.append(list(map(int, list(input()))))
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]
                break
        if maze[i][j] == 2:
            break
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 3:
                end = [i, j]
                break
        if maze[i][j] == 2:
            break
    visited = [[0 for i in range(n)] for j in range(n)]
    BFS(maze, [start], 1)
    if visited[end[0]][end[1]] == 0:
        result = 0
    else:
        result = visited[end[0]][end[1]] - 2
    print('#{} {}'.format(tc, result))
