def solution(strings):
    answer = True
    
    stack = []
    for string in strings:
        if len(stack) > 0:
            if string == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(string)
            else:
                stack.append(string)
        else:
            stack.append(string)
                
    if len(stack) != 0:
        return False
    return True