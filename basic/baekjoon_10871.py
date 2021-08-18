n, x = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
for num in nums:
    if x > num:
        print("{}".format(num), end=" ")