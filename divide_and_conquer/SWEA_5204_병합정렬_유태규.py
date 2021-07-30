def merge_sort(nums):
    if len(nums) == 1:
        return nums
    middle = len(nums) // 2
    left = nums[0: middle]
    right = nums[middle:len(nums)]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global lcnt
    result = [-1] * (len(left) + len(right))
    if right[-1] < left[-1]:
        lcnt += 1
    l = 0
    r = 0
    idx = 0
    while 1:
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result[idx] = left[l]
                idx += 1
                l += 1
            else:
                result[idx] = right[r]
                idx += 1
                r += 1
        elif l < len(left):
            result[idx] = left[l]
            idx += 1
            l += 1
        elif r < len(right):
            result[idx] = right[r]
            idx += 1
            r += 1
        else:
            break
    return result


for tc in range(1, 1 + int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    lcnt = 0
    result = merge_sort(nums)
    print('#{} {} {}'.format(tc, result[n // 2], lcnt))
