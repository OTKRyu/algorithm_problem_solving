import sys

input = sys.stdin.readline

def per(step):
    if step == n:
        print(*permutation)
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                permutation.append(i)
                check[i] = 1
                per(step+1)
                check[i] = 0
                permutation.pop()



n = int(input())
check = [0 for i in range(n+1)]
permutation = []
per(0)