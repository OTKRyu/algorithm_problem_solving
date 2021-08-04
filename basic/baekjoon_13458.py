import sys

input = sys.stdin.readline


n = int(input())
As = list(map(int, input().split()))
b, c = map(int, input().split())
total = 0
for i in range(n):
    flag = 1
    if As[i] - b > 0:
        total += 1
        total += (As[i] - b)//c
        if (As[i]-b)%c:
            total += 1
    else:
        total += 1
print(total)