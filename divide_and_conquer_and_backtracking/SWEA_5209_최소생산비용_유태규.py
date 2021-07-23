def dfs(cr, cs):
    global result, n
    if cr == n:
        if result > cs:
            result = cs
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                cs += nums[cr][i]
                if cs < result:
                    dfs(cr + 1, cs)
                cs -= nums[cr][i]
                check[i] = 0


for tc in range(1, 1 + int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for i in range(n)]
    result = 100 * n
    check = [0 for j in range(n)]
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
