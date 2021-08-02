import sys

tc = int(sys.stdin.readline())
for i in range(tc):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(a+b)
