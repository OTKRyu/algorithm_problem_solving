def dfs(p,total):
    global n, result
    total += nums[p[0]][p[1]]
    if p == [n-1,n-1]:
        if result > total:
            result = total
    else:
        if result < total:
            return
        else:
            np = [p[0]+1,p[1]]
            if np[0]<=n-1:
                dfs(np,total)

            np = [p[0],p[1]+1]
            if np[1] <=n-1:
                dfs(np,total)


for tc in range(1,1+int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for i in range(n)]
    result = 11*2*n
    s = [0,0]
    dfs(s,0)
    print('#{} {}'.format(tc, result))