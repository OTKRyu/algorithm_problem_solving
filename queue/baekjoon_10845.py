import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    tmp = str(input())
    if tmp.startswith('push'):
        tmp = tmp.split()
        q.append(int(tmp[1]))
    elif tmp.startswith('pop'):
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif tmp.startswith('size'):
        print(len(q))
    elif tmp.startswith('empty'):
        if len(q):
            print(0)
        else:
            print(1)
    elif tmp.startswith('front'):
        if len(q):
            print(q[0])
        else:
            print(-1)
    else:
        if len(q):
            print(q[-1])
        else:
            print(-1)