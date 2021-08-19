import sys

stack = []
for tc in range(int(input())):
    o = sys.stdin.readline()
    top = 0
    if o.startswith('push'):
        tmp = list(o.split())
        stack.append(int(tmp[1]))
    elif o.startswith('pop'):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif o.startswith('size'):
        print(len(stack))
    elif o.startswith('empty'):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])