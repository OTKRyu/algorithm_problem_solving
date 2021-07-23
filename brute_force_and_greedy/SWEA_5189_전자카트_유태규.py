def per(n,m):
    global answer
    if len(result) == m:
        loss = 0
        result.append(0)
        for i in range(n):
            loss += losses[result[i]][result[i+1]]
        if answer > loss:
            answer = loss
        result.pop()
        result.pop()
        return
    else:
        for i in range(n):
            if check[i] == 0:
                result.append(ns[i])
                check[i] = 1
                per(n,m)
                check[i] = 0
        else:
            if len(result) != 0:
                result.pop()
                return


for tc in range(1, 1 + int(input())):
    n = int(input())
    losses = [list(map(int, input().split())) for _ in range(n)]
    answer = 101 * n
    result = [0]
    check = [0 for i in range(n)]
    check[0] = 1
    ns = list(range(n))
    per(n,n)
    print('#{} {}'.format(tc, answer))
