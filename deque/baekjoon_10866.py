from collections import deque
from sys import stdin
input = stdin.readline
d = deque()
for i in range(int(input())):
    tmp = input()
    if tmp.startswith('push_back'):
        ttmp = tmp.split()
        d.append(int(ttmp[1]))
    elif tmp.startswith('push_front'):
        ttmp = tmp.split()
        d.appendleft(int(ttmp[1]))
    elif tmp.startswith('front'):
        if len(d):
            print(d[0])
        else:
            print(-1)
    elif tmp.startswith('back'):
        if len(d):
            print(d[-1])
        else:
            print(-1)
    elif tmp.startswith('size'):
        print(len(d))
    elif tmp.startswith('empty'):
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif tmp.startswith('pop_front'):
        if len(d):
            print(d.popleft())
        else:
            print(-1)
    else:
        if len(d):
            print(d.pop())
        else:
            print(-1)