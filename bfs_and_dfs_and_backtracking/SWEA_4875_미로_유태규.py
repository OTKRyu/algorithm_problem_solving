def search(g, v):
    visited[v[0]][v[1]] = 1
    if g[v[0]][v[1]] == 3:
        return 1
    ps = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= v[0] + dy[i] < n and 0 <= v[1] + dx[i] < n and g[v[0] + dy[i]][v[1] + dx[i]] in [0, 3] and \
                visited[v[0] + dy[i]][v[1] + dx[i]] == 0:
            ps.append([v[0] + dy[i], v[1] + dx[i]])
    if len(ps) == 0:
        return 0
    else:
        for p in ps:
            if search(g, p):
                return 1
        else:
            return 0


for tc in range(1, int(input())+1):
    n = int(input())
    maze = []
    visited = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        maze.append(list(map(int, list(input()))))
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]
                break
        if maze[i][j] == 2:
            start = [i, j]
            break
    print('#{} {}'.format(tc, search(maze, start)))
