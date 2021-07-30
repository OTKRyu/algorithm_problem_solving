for tc in range(1, int(input())+1):
    stack = []
    tmps = input().split()
    tmps.pop()
    for tmp in tmps:
        try:
            if tmp == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif tmp == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tmp == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif tmp == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            else:
                stack.append(int(tmp))
        except:
            print('#{} error'.format(tc))
            break
    else:
        if len(stack) == 1:
            print('#{} {}'.format(tc, stack[-1]))
        else:
            print('#{} error'.format(tc))
