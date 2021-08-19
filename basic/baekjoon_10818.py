numslen = int(input())
nums = list(map(int, input().split()))
for i in range(numslen):
    if i == 0:
        maxnum = nums[i]
        minnum = nums[i]
    else:
        if maxnum < nums[i]:
            maxnum = nums[i]
        if minnum > nums[i]:
            minnum = nums[i]
print("{} {}".format(minnum, maxnum))
