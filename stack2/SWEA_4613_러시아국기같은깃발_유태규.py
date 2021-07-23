def DFS(flag, n, m , cl , col, total):
    global minimum
    if cl == n:
        if total < minimum:
            minimum = total
    else:
        if col == 'W':
            if cl < n-3:
                ps = ['W', 'B']
                total += m - flag[cl].count(col)
                if total < minimum:
                    for p in ps:
                        DFS(flag, n, m, cl + 1, p, total)
                total -= m - flag[cl].count(p)
            else:
                total += m - flag[cl].count('W')
                if total < minimum:
                    DFS(flag, n, m, cl + 1, 'B', total)
                total -= m - flag[cl].count('W')
        elif col == 'B':
            if cl < n-2:
                ps = ['B', 'R']
                total += m - flag[cl].count(col)
                if total < minimum:
                    for p in ps:
                        DFS(flag, n, m, cl + 1, p, total)
                total -= m - flag[cl].count(col)
            else:
                total += m - flag[cl].count('B')
                if total < minimum:
                    DFS(flag, n, m, cl + 1, 'R', total)
                total -= m - flag[cl].count('B')
        else:
            total += m - flag[cl].count(col)
            if total < minimum:
                DFS(flag, n, m, cl + 1, col, total)
            total -= m - flag[cl].count(col)

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    flag = []
    for i in range(n):
        flag.append(list(input()))
    minimum = 1000000000
    DFS(flag,n,m,0,'W',0)
    print('#{} {}'.format(tc, minimum))