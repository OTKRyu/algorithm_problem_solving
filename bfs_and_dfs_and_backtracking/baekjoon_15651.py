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
            result.append(ns[i])
            per(n,m, cl+1)
        else:
            if len(result) != 0:
                result.pop()
                return
per(n,m,0)