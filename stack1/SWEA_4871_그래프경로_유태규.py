class Stack:
    def __init__(self):
        self.real = []
        self.top = -1

    def push(self, ele):
        self.real.append(ele)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return None
        else:
            result = self.real[self.top]
            self.real.pop()
            self.top -= 1
            return result

    def peek(self):
        if self.top == -1:
            return None
        else:
            result = self.real[self.top]
            return result

    def is_empty(self):
        if self.top == -1:
            return 1
        else:
            return 0


def DFS(gs, sp, ep):
    s = Stack()
    v = sp
    visited = list()
    visited.append(v)
    s.push(v)
    while s.top != -1:
        for g in gs:
            if g[0] == v and g[1] not in visited:
                visited.append(g[1])
                s.push(g[1])
                v = g[1]
                if v == ep:
                    return 1
                break
        else:
            v = s.pop()
    else:
        return 0



for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    gs = []
    for i in range(e):
        tmps, tmpe = map(int, input().split())
        gs.append((tmps, tmpe))
    sp, ep = map(int, input().split())
    print('#{} {}'.format(tc, DFS(gs, sp, ep)))
