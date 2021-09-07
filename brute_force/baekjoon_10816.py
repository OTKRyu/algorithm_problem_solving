import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
finds = list(map(int, sys.stdin.readline().split()))
cnt = {}
for num in nums:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

print(' '.join(str(cnt[find]) if find in cnt else '0' for find in finds))