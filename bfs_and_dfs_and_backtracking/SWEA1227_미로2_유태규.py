def BFS(g, s):
    visited[s[0]][s[1]] = 1
    queue = []
    queue.append(s)
    while queue:
        v = queue.pop(0)
        for p in search(g,v):
            if not visited[p[0]][p[1]]:
                queue.append(p)
                visited[p[0]][p[1]] = 1


def search(g, v):
    ps = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= v[0] + dy[i] < n and 0 <= v[1] + dx[i] < n and g[v[0] + dy[i]][v[1] + dx[i]] in [0, 3] and \
                visited[v[0] + dy[i]][v[1] + dx[i]] == 0:
            ps.append([v[0] + dy[i], v[1] + dx[i]])
    return ps


for _ in range(10):
    tc = int(input())
    n = 100
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
        if maze[i][j] == 3:
            break
    BFS(maze, start)
    print('#{} {}'.format(tc, visited[end[0]][end[1]]))