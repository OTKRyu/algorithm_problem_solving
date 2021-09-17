from collections import deque

for tc in range(1,1+int(input())):
    orders = list(input())
    n = int(input())
    tmp = input()
    tmp = tmp[1:-1]
    if tmp:
        d = deque(list(map(int, tmp.split(','))))
    else:
        d = deque([])
    flag = 1
    for order in orders:
        if order == 'R':
            if flag:
                flag = 0
            else:
                flag = 1
        else:
            if len(d):
                if flag:
                    d.popleft()
                else:
                    d.pop()
            else:
                print('error')
                break
    else:
        if flag:
            result = list(d)
            for i in range(len(result)+2):
                if i==0:
                    print('[',end='')
                elif i == len(result)+1:
                    print(']')
                elif i == len(result):
                    print(result[i-1],end='')
                else:
                    print(result[i-1], end=',')
        else:
            d.reverse()
            result = list(d)
            for i in range(len(result) + 2):
                if i == 0:
                    print('[', end='')
                elif i == len(result) + 1:
                    print(']')
                elif i == len(result):
                    print(result[i - 1], end='')
                else:
                    print(result[i - 1], end=',')