n = int(input())
nums = list(map(int, input().split()))
nums = list(set(list(nums)))
nums.sort()
print(*nums)