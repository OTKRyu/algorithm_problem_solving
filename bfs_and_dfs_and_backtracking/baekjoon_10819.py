import sys

input = sys.stdin.readline

def per(step):
    global maxima
    if step == n:
        total = 0
        for i in range(n-1):
            total += abs(permutation[i]-permutation[i+1])
        if total > maxima:
            maxima = total
    else:
        for i in range(n):
            if check[i] == 0:
                permutation.append(nums[i])
                check[i] = 1
                per(step+1)
                check[i] = 0
                permutation.pop()

n = int(input())
check = [0 for i in range(n)]
nums = list(map(int, input().split()))
permutation = []
maxima = 0
per(0)
print(maxima)