import sys

input = sys.stdin.readline

def binary(num):
    s = 1
    e = num
    while e>=s:
        m = (e+s)//2
        if m**2 == num:
            return m
        elif m**2 > num:
            e = m-1
        else:
            s = m+1


n = int(input())
print(binary(n))
