cnt = 0 
def dfs(step,numbers, target, result):
    global cnt
    if step == len(numbers):
        if result == target:
            cnt += 1
            return
    else:
        dfs(step+1, numbers, target, result + numbers[step])
        dfs(step+1, numbers, target, result - numbers[step])
def solution(numbers, target):
    dfs(0,numbers, target, 0)
    return cnt