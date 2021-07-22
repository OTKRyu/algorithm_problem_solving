def back(tokens):
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, }
    s = []
    result = []
    for token in tokens:
        if icp.get(token) == None:
            result += token
        else:
            if len(s) == 0:
                s.append(token)
            else:
                while len(s) != 0 and icp.get(token) <= icp.get(s[-1]):
                    result.append(s.pop())
                s.append(token)
    else:
        while len(s) != 0:
            result.append(s.pop())
    return result


def iter(tokens):
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, }
    s = []
    for token in tokens:
        if icp.get(token) == None:
            s.append(token)
        else:
            if token == '+':
                x = int(s.pop())
                y = int(s.pop())
                s.append(x + y)
            elif token == '-':
                x = int(s.pop())
                y = int(s.pop())
                s.append(y - x)
            elif token == '*':
                x = int(s.pop())
                y = int(s.pop())
                s.append(x * y)
            else:
                x = int(s.pop())
                y = int(s.pop())
                s.append(y / x)
    else:
        return s.pop()


for tc in range(1, 11):
    length = int(input())
    target = list(input())
    print('#{} {}'.format(tc, iter(back(target))))
