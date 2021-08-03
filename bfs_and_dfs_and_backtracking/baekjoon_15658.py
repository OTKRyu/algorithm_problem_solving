def dfs(step, state):
    global maxima, minima
    if step == n-1:
        if state > maxima:
            maxima = state
        if state < minima:
            minima = state
    else:
        if iters[0] > 0:
            iters[0] -= 1
            dfs(step+1, state + nums[step+1])
            iters[0] += 1
        if iters[1] > 0:
            iters[1] -= 1
            dfs(step+1, state - nums[step+1])
            iters[1] += 1
        if iters[2] > 0:
            iters[2] -= 1
            dfs(step+1, state * nums[step+1])
            iters[2] += 1
        if iters[3] > 0:
            if state >= 0:
                iters[3] -= 1
                dfs(step+1, state // nums[step+1])
                iters[3] += 1
            else:
                iters[3] -= 1
                state *= -1
                state //= nums[step+1]
                state *= -1
                dfs(step+1, state)
                iters[3] += 1




n = int(input())
nums = list(map(int, input().split()))
iters = list(map(int, input().split()))
maxima = -1100000000
minima =  1100000000
dfs(0, nums[0])
print(maxima)
print(minima)