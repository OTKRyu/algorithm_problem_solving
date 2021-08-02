n, m = map(int,input().split())
result = []
check = [0] * n
ns = list(range(1,n+1))

def per(n,m, cl):
    if len(result) == m:
        print(*result)
        result.pop()
        return
    else:
        for i in range(n):
            if check[i] == 0:
                result.append(ns[i])
                check[i] = 1
                per(n,m, cl+1)
                check[i] = 0
        else:
            if len(result) != 0:
                result.pop()
                return
per(n,m,0)