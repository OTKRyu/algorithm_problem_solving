n = int(input())
nums = list(map(int,input().split()))
nums.sort()
total = 0
for i in range(len(nums)):
    total += nums[i]*(len(nums)-i)
print(total)