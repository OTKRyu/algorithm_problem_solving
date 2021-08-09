import sys

input = sys.stdin.readline
n = int(input())
bits = 0
for i in range(n):
    order = input().split()
    if order[0].startswith('add'):
        tmp = int(order[1])
        if bits & (1 << tmp):
            continue
        else:
            bits += 1 << tmp
    elif order[0].startswith('remove'):
        tmp = int(order[1])
        if bits & 1 << tmp:
            bits -= 1 << tmp
    elif order[0].startswith('check'):
        tmp = int(order[1])
        if bits & (1 << tmp):
            print(1)
        else:
            print(0)
    elif order[0].startswith('toggle'):
        tmp = int(order[1])
        if bits & 1 << tmp:
            bits -= 1 << tmp
        else:
            bits += 1 << tmp
    elif order[0].startswith('all'):
        bits = (1 << 21) - 1
    else:
        bits = 0