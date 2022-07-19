def solution(strings):
    answer = -1
    stack = []
        
    for string in strings:
        stack.append(string)
        while 1:
            if len(stack) < 2:
                break
            
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                break
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer