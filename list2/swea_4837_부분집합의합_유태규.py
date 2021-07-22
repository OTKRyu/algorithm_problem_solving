def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total


tcs = int(input())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, tcs + 1):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    k = tmp[1]
    count = 0
    for i in range(1 << 12):
        tmps = []
        for j in range(len(a)):
            if i & (1 << j):
                tmps.append(a[j])
        if len(tmps) == n and my_sum(tmps) == k:
            count += 1
    print('#{} {}'.format(tc, count))
