import sys

input = sys.stdin.readline

def dfs(step,dwarfs):
    if dwarfs == 7:
        if sum(result) == 100:
            result.sort()
            for i in range(7):
                print(result[i])
    else:
        if step > 8:
            return
        else:
            result.append(heights[step])
            dfs(step+1, dwarfs+1)
            result.pop()
            dfs(step+1, dwarfs)

heights = [int(input()) for i in range(9)]
result = []
dfs(0,0)
