arr = list(map(int, input().split()))
n = len(arr)


def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total


for i in range(1 << n):
    tmp = []
    for j in range(n):
        if i & (1 << j):
            tmp.append(arr[j])
    if my_sum(tmp) == 10:
        print(tmp)