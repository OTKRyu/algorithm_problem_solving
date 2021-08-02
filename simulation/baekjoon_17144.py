import sys

input = sys.stdin.readline
dr = [0,-1,0,1]
dc = [1,0,-1,0]
def diffuse():
    tmp = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if dusts[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0<=nr< r and 0<=nc<c and dusts[nr][nc] != -1:
                        tmp[nr][nc] += dusts[i][j] //5
                        cnt += 1
                else:
                    dusts[i][j] -= (dusts[i][j] //5) * cnt
    for i in range(r):
        for j in range(c):
            dusts[i][j] += tmp[i][j]
def clean():
    upper = [conditioner[0],0]
    lower = [conditioner[1],0]
    cr = conditioner[0]
    cc = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(c-1):
        tmp1 = dusts[cr][cc+1]
        dusts[cr][cc+1] = tmp2
        tmp2 = tmp1
        cc += 1
    for i in range(upper[0]):
        tmp1 = dusts[cr-1][cc]
        dusts[cr-1][cc] = tmp2
        tmp2 = tmp1
        cr -= 1
    for i in range(c-1):
        tmp1 = dusts[cr][cc - 1]
        dusts[cr][cc - 1] = tmp2
        tmp2 = tmp1
        cc -= 1
    for i in range(upper[0]):
        if dusts[cr+1][cc] == -1:
            continue
        else:
            tmp1 = dusts[cr + 1][cc]
            dusts[cr + 1][cc] = tmp2
            tmp2 = tmp1
            cr += 1
    cr = conditioner[1]
    cc = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(c - 1):
        tmp1 = dusts[cr][cc + 1]
        dusts[cr][cc + 1] = tmp2
        tmp2 = tmp1
        cc += 1
    for i in range(r-lower[0]-1):
        tmp1 = dusts[cr + 1][cc]
        dusts[cr + 1][cc] = tmp2
        tmp2 = tmp1
        cr += 1
    for i in range(c - 1):
        tmp1 = dusts[cr][cc - 1]
        dusts[cr][cc - 1] = tmp2
        tmp2 = tmp1
        cc -= 1
    for i in range(r-lower[0]-1):
        if dusts[cr-1][cc] == -1:
            continue
        else:
            tmp1 = dusts[cr - 1][cc]
            dusts[cr - 1][cc] = tmp2
            tmp2 = tmp1
            cr -= 1

r,c,t = map(int, input().split())
dusts = [list(map(int, input().split())) for i in range(r)]
conditioner = []
for i in range(r):
    if dusts[i][0] == -1:
        conditioner.append(i)
for i in range(t):
    diffuse()
    clean()
result = 0
for i in range(r):
    for j in range(c):
        if dusts[i][j] != -1:
            result += dusts[i][j]
print(result)