import sys

input = sys.stdin.readline

def per(step):
    if step == m:
        print(*permutation)
        return

    if permutation:
        for i in range(n):
            if permutation[-1] <= nums[i]:
                permutation.append(nums[i])
                per(step+1)
                permutation.pop()
    else:
        for i in range(n):
            permutation.append(nums[i])
            per(step+1)
            permutation.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
permutation = []
per(0)
