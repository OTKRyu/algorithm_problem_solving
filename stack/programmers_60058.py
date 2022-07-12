def solution(p):
    if p == '':
        return p
    
    stack = 0
    position = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            position = i
            break
    u = p[0:position+1]
    v = p[position+1: len(p)]
    stack = 0
    position = 0
    flag = 1
    for i in range(len(u)):
        if u[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            flag = 0
            break
    if flag == 1:
        return u + solution(v)
    u = u[1:len(u)-1]
    new_u = ''
    for s in u:
        if s == "(":
            new_u += ")"
        else:
            new_u += "("
    return '(' + solution(v) + ")" + new_u