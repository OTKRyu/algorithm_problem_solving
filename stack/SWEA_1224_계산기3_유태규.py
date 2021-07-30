def iter(tokens):
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, }
    s = []
    for token in tokens:
        if icp.get(token) == None:
            s.append(token)
        else:
            if token == '+':
                x = int(s.pop())
                y = int(s.pop())
                s.append(x + y)
            elif token == '-':
                x = int(s.pop())
                y = int(s.pop())
                s.append(y - x)
            elif token == '*':
                x = int(s.pop())
                y = int(s.pop())
                s.append(x * y)
            else:
                x = int(s.pop())
                y = int(s.pop())
                s.append(y / x)
    else:
        return s.pop()


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


icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ')': -1}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': -1}

for tc in range(1, 11):
    n = int(input())
    tokens = list(input())
    s = Stack()
    result = ''
    idx = 0
    e_idx = len(tokens)
    while 1:
        if idx == e_idx:
            while not s.is_empty:
                result += s.pop()
            break
        if icp.get(tokens[idx]) == None:
            result += tokens[idx]
            idx += 1
        else:
            if icp.get(tokens[idx]) == -1:
                while s.peek() != '(':
                    result += s.pop()
                s.pop()
                idx += 1
            else:
                if len(s.real) == 0:
                    s.push(tokens[idx])
                    idx += 1
                else:
                    while len(s.real) != 0 and icp.get(tokens[idx]) <= isp.get(s.real[-1]):
                        result += s.pop()
                    s.push(tokens[idx])
                    idx += 1
    print('#{} {}'.format(tc, iter(result)))