import sys
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


for tc in range(1, int(input())+1):
    tmp = list(sys.stdin.readline())
    tmp.pop()
    s = Stack()
    for i in range(len(tmp)):
        if tmp[i] == ')':
            if s.peek() == '(':
                s.pop()
            else:
                print('NO')
                break
        else:
            s.push(tmp[i])
    else:
        if s.is_empty():
            print('YES')
        else:
            print('NO')