def dfs(cr, cs):
    global result, n
    if cr == n:
        if result < cs:
            result = cs
    else:
        for i in range(n):
            tmp = cs
            if check[i] == 0 and nums[cr][i] != 0:
                check[i] = 1
                tmp *= nums[cr][i]
                if result < tmp:
                    dfs(cr + 1, tmp)
                check[i] = 0


for tc in range(1, 1 + int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            nums[i][j] /= 100
    result = 0.0
    check = [0 for j in range(n)]
    dfs(0, 1)
    result = round(result*100, 6)
    print('#{} {:6f}'.format(tc, result))
