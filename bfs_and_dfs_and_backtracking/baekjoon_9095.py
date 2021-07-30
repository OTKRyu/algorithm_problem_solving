import sys

input = sys.stdin.readline

def dfs(n):
    global cnt
    if n == 0:
        cnt += 1
        return
    if n < 0:
        return
    for i in range(3):
        dfs(n-i-1)

for tc in range(int(input())):
    cnt = 0
    n = int(input())
    dfs(n)
    print(cnt)