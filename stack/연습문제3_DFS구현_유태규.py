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
# class Stack:
#     def __init__(self,n):
#         self.top = -1
#         self.stack = [0]*n
#
#     def push(self,data):
#         if self.top == len(self.stack) - 1:
#             return None
#         self.top += 1
#         self.stack[self.top] = data
#
#     def pop(self):
#         if self.top == -1:
#             return None
#         self.top -= 1
#         return self.stack[self.top+1]


def DFS(gs, sp):
    s = Stack()
    v = sp
    visited = []
    visited.append(v)
    s.push(v)
    while len(visited) != 8:
        for g in gs:
            if g[0] == v and g[1] not in visited:
                visited.append(g[1])
                s.push(g[1])
                v = g[1]
                print(s.real)
                print(visited)
                break
        else:
            v = s.pop()
            print(s.real)
            print(v)


tmp = []
sp = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(9):
    tmp.append(tuple(map(int, input().split())))
for i in range(9):
    (t_tmp_y, t_tmp_x) = tmp[i]
    tmp.append((t_tmp_x, t_tmp_y))
DFS(tmp, 1)
