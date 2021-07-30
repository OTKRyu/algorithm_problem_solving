import sys

input = sys.stdin.readline

def combination(idx, sidx):
    global result, b
    if sidx == 6:
        print(*comb)
        return
    if idx == n:
        return
    comb[sidx] = nums[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


while 1:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    n = nums.pop(0)
    comb = [0 for i in range(6)]
    combination(0,0)
    print()
