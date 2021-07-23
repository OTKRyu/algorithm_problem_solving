class MinHeap:
    def __init__(self, n):
        self.n = n
        self.array = [0]

    def push(self, num):
        self.array.append(num)
        l = len(self.array) - 1
        while l // 2 != 0:
            if self.array[l] < self.array[l // 2]:
                tmp = self.array[l]
                self.array[l] = self.array[l // 2]
                self.array[l // 2] = tmp
                l = l // 2
            else:
                break

    def result(self):
        s = len(self.array) - 1
        total = 0
        while s // 2 != 0:
            s = s // 2
            total += self.array[s]
        return total


for tc in range(1, 1 + int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = MinHeap(n)
    for num in nums:
        heap.push(num)
    print('#{} {}'.format(tc, heap.result()))
