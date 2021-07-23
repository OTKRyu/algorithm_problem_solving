def my_max(nums):
    for i in range(len(nums)):
        if i == 0:
            maximum = nums[i]
        else:
            if maximum < nums[i]:
                maximum = nums[i]
    return maximum

for tc in range(1, int(input()) + 1):
    n = input()
    m = input()
    tmp = dict()
    for char in m:
        if char in n:
            if tmp.get(char):
                tmp[char] += 1
            else:
                tmp[char] = 1
    result = list(tmp.values())
    print('#{} {}'.format(tc, my_max(result)))
