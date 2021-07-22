def dfs(c):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    possibles = []
    lm = 0
    for i in range(4):
        nc = [c[0] + dy[i], c[1] + dx[i]]
        if 0 <= nc[0] < n and 0 <= nc[1] < n and nums[nc[0]][nc[1]] - nums[c[0]][c[1]] == 1:
            possibles.append(nc)
    if possibles:
        for possible in possibles:
            if check[possible[0]][possible[1]] == 0:
                cnt = dfs(possible)
                if cnt > lm:
                    lm = cnt
            else:
                if lm < check[possible[0]][possible[1]] + 1:
                    lm = check[possible[0]][possible[1]] + 1
        check[c[0]][c[1]] = lm
        return lm + 1
    else:
        check[c[0]][c[1]] = 1
        return 2


for tc in range(1, 1 + int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for i in range(n)]
    m_move = 0
    m_p = [0, 0]
    check = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                dfs([i, j])
            if m_move == check[i][j]:
                if nums[m_p[0]][m_p[1]] > nums[i][j]:
                    m_p = [i, j]
            elif m_move < check[i][j]:
                m_move = check[i][j]
                m_p = [i, j]
    print('#{} {} {}'.format(tc, nums[m_p[0]][m_p[1]], m_move))
