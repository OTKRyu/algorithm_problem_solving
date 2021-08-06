import sys

input = sys.stdin.readline

heap = [0] * 100000
h_cnt = 0
for i in range(int(input())):
    tmp = int(input())
    if tmp == 0:
        if h_cnt == 0:
            print(0)
        else:
            print(heap[1])
            heap[1], heap[h_cnt] = heap[h_cnt], heap[1]
            h_cnt -= 1
            cl = 1
            while 1:
                if 2 * cl + 1 <= h_cnt:
                    if heap[2 * cl] <= heap[2 * cl + 1]:
                        target = 2 * cl + 1
                    else:
                        target = 2 * cl
                    if heap[cl] < heap[target]:
                        heap[cl], heap[target] = heap[target], heap[cl]
                        cl = target
                    else:
                        break
                elif 2 * cl == h_cnt:
                    if heap[cl] < heap[2 * cl]:
                        heap[cl], heap[2 * cl] = heap[2 * cl], heap[cl]
                        cl = 2 * cl
                    else:
                        break
                else:
                    break
    else:
        h_cnt += 1
        heap[h_cnt] = tmp
        l = h_cnt
        while l // 2 != 0:
            if heap[l] > heap[l // 2]:
                tmp = heap[l]
                heap[l] = heap[l // 2]
                heap[l // 2] = tmp
                l = l // 2
            else:
                break