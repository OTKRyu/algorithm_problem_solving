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
s = Stack()
for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num == 0:
        s.pop()
    else:
        s.push(num)
print(sum(s.real))