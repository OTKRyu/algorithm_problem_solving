class Stack:
    def __init__(self):
        self.real = []
        self.top = -1

    def push(self, ele):
        self.real.append(ele)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return 0
        else:
            result = self.real[self.top]
            self.real.pop()
            self.top -= 1
            return result

    def peek(self):
        if self.top == -1:
            return 0
        else:
            result = self.real[self.top]
            return result

    def is_empty(self):
        if self.top == -1:
            return 1
        else:
            return 0


for tc in range(1, int(input())+1):
    tmp = list(input())
    actual = []
    for i in range(len(tmp)):
        if tmp[i] in ['{','}','(',')']:
            actual.append(tmp[i])
    s = Stack()
    for i in range(len(actual)):
        if actual[i] == '}':
            if s.peek() == '{':
                s.pop()
            else:
                print('#{} {}'.format(tc, 0))
                break
        elif actual[i] == ')':
            if s.peek() == '(':
                s.pop()
            else:
                print('#{} {}'.format(tc, 0))
                break
        else:
            s.push(actual[i])
    else:
        print('#{} {}'.format(tc, s.is_empty()))