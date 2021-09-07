import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
total = 0
for i in range(n):
    total = 0
    total += nums[i]
    if total == m:
        cnt += 1
    else:
        for j in range(i+1,n):
            total += nums[j]
            if total == m:
                cnt += 1
                break
            elif total > m:
                break
print(cnt)