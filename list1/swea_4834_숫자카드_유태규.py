def my_count(numbers, number):
    count = 0
    for num in numbers:
        if num == number:
            count += 1
    return count


def my_max(nums):
    max_num = 0
    for num in nums:
        if max_num < num:
            max_num = num
    return max_num


for tc in range(1, int(input())+1):
    length = int(input())
    nums = list(map(int, input()))
    max_count = 0
    max_actual = 0
    for num in nums:
        if my_count(nums, num) > max_count:
            max_count = my_count(nums, num)
            max_actual = num
    if max_count == 1:
        max_actual = my_max(nums)
    print("#{} {} {}".format(tc, max_actual, max_count))
