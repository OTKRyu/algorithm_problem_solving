def my_min(nums):
    mv = 0
    for i in range(len(nums)):
        if i == 0:
            mv = nums[i]
        elif mv > nums[i]:
            mv = nums[i]
    return mv


def my_max(nums):
    mv = 0
    for i in range(len(nums)):
        if mv < nums[i]:
            mv = nums[i]
    return mv


for tc in range(1, int(input())+1):
    length = int(input())
    nums = list(map(int, input().split()))
    print("#{} {}".format(tc, my_max(nums)-my_min(nums)))
