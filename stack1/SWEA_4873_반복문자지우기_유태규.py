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
    chars = list(input())
    s = Stack()
    for i in range(len(chars)):
        s.push(chars[i])
        while len(s.real) > 1:
            if s.real[s.top] != s.real[s.top-1]:
                break
            else:
                s.pop()
                s.pop()
    print('#{} {}'.format(tc,len(s.real)))
