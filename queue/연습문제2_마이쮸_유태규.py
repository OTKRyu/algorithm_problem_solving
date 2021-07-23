class queue:
    def __init__(self,n):
        self.length = n
        self.real = [0]*self.length
        self.front = -1
        self.rear = -1
    def is_empty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0
    def is_full(self):
        if self.rear == self.length-1:
            return 1
        else:
            return 0
    def en_queue(self,item):
        if self.is_full():
            print('queue is already full')
        else:
            self.rear += 1
            self.real[self.rear] = item
    def de_queue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            self.front += 1
            return self.real[self.front]
    def peek(self):
        if self.is_empty():
            print('queue is empty')
        else:
            return self.real[self.front+1]

n = 10
q= queue(100)
i = 1
while n>0:
    q.en_queue([i,1])
    tmp = q.de_queue()
    n -= tmp[1]
    tmp[1] += 1
    q.en_queue(tmp)
    i += 1
print(q.real[q.rear][0])