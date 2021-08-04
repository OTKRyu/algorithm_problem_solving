import sys

input = sys.stdin.readline

def dfs(date, total):
    global maxima
    if date == n+1:
        if maxima < total:
            maxima = total
    else:
        if date + tasks[date][0] > n+1:
            dfs(n+1, total)
        else:
            dfs(date + tasks[date][0], total + tasks[date][1])
        dfs(date + 1, total)


n = int(input())
tasks = [[0,0]]
for i in range(n):
    tasks.append(list(map(int, input().split())))
maxima = 0
dfs(1,0)
print(maxima)