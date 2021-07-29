import sys
class queue:
    def __init__(self, n):
        self.length = n
        self.real = [0] * self.length
        self.front = -1
        self.rear = -1

    def is_empty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    def is_full(self):
        if self.rear == self.length - 1:
            return 1
        else:
            return 0

    def en_queue(self, item):
        if self.is_full():
            print('queue is already full')
        else:
            self.rear += 1
            self.real[self.rear] = item

    def de_queue(self):
        if self.is_empty():
            return -1
        else:
            self.front += 1
            return self.real[self.front]

    def peek(self):
        if self.is_empty():
            return -1
        else:
            return self.real[self.front + 1]


n = int(sys.stdin.readline().rstrip())
q = queue(n)
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    if tmp.startswith('push'):
        q.en_queue(int(tmp.split()[1]))
    elif tmp == 'pop':
        print(q.de_queue())
    elif tmp == 'size':
        print(q.rear - q.front)
    elif tmp == 'empty':
        print(q.is_empty())
    elif tmp == 'front':
        print(q.peek())
    else:
        if q.is_empty():
            print(-1)
        else:
            print(q.real[q.rear])
