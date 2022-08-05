from collections import deque

def checker(chars):
    stack = []
    for char in chars:
        stack.append(char)
        while 1:
            if len(stack) >= 2:
                if stack[-1] == "}" and stack[-2] == "{":
                    stack.pop()
                    stack.pop()
                elif stack[-1] == "]" and stack[-2] == "[":
                    stack.pop()
                    stack.pop()
                elif stack[-1] == ")" and stack[-2] == "(":
                    stack.pop()
                    stack.pop()
                else:
                    break
            else:
                break
    if len(stack) == 0:
        return 1
    return 0

def solution(s):
    answer = 0
    q = deque(list(s))
    for i in range(len(s)):
        tmp = q.popleft()
        q.append(tmp)
        answer += checker(list(q))
        checker(list(q))
    return answer