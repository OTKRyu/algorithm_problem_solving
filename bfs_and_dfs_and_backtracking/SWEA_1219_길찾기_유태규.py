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


def DFS(ls, sp, ep):
    s = Stack()
    v = sp
    visited = [0] * 100
    visited[v] = 1
    s.push(v)
    while s.top != -1:
        if v == ep:
            return 1
        else:
            if gs[v]:
                if visited[gs[v][0]] == 0:
                    v = gs[v][0]
                    visited[v] = 1
                    s.push(v)
                elif len(gs[v]) > 1 and visited[gs[v][1]] == 0:
                    v = gs[v][1]
                    visited[v] = 1
                    s.push(v)
                else:
                    v = s.pop()
            else:
                v = s.pop()
    else:
        return 0


for _ in range(10):
    tc, length = map(int, input().split())
    tmp = list(map(int, input().split()))
    lines = []
    for i in range(0, 2 * length - 1, 2):
        lines.append((tmp[i], tmp[i + 1]))
    gs = [[] for i in range(100)]
    for line in lines:
        gs[line[0]].append(line[1])
    print('#{} {}'.format(tc, DFS(gs, 0, 99)))
