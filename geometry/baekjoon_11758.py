import sys

input = sys.stdin.readline


def ccw():
    a = [dots[1][0] - dots[0][0], dots[1][1] - dots[0][1]]
    b = [dots[2][0] - dots[0][0], dots[2][1] - dots[0][1]]
    if a[0] * b[1] - a[1] * b[0] > 0:
        return 1
    elif a[0] * b[1] - a[1] * b[0] < 0:
        return -1
    else:
        return 0


dots = [list(map(int, input().split())) for i in range(3)]
print(ccw())
