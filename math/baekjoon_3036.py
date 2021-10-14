def gcd(a, b):
    tmp_a = a
    tmp_b = b
    while (tmp_b != 0):
        tmp_a = tmp_a % tmp_b
        tmp_a, tmp_b = tmp_b, tmp_a
    return tmp_a


n = int(input())
nums = list(map(int, input().split()))
for i in range(1, n):
    print('{}/{}'.format(nums[0] // gcd(nums[0], nums[i]), nums[i] // gcd(nums[0], nums[i])))