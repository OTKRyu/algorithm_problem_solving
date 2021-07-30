def my_max(nums):
    mmax = 0
    for num in nums:
        if mmax < num:
            mmax = num
    return mmax


def my_min(nums):
    mmin = 100
    for num in nums:
        if mmin > num:
            mmin = num
    return mmin


for tc in range(1, 11):
    maximum = int(input())
    nums = list(map(int, input().split()))
    for i in range(maximum):
        for j in range(len(nums)):
            if my_max(nums) == nums[j]:
                nums[j] -= 1
                break
        for j in range(len(nums)):
            if my_min(nums) == nums[j]:
                nums[j] += 1
                break
    print("#{} {}".format(tc, my_max(nums)-my_min(nums)))
