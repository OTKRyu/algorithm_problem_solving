import sys

input = sys.stdin.readline

def per(step):
    if step == m:
        print(*permutation)
        return

    for i in range(n):
        if check[i] == 0:
            permutation.append(nums[i])
            check[i] = 1
            per(step+1)
            check[i] = 0
            permutation.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
permutation = []
check = [0 for i in range(n)]
per(0)
