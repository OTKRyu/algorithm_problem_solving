def bin_to_ten(num):
    ten = 0
    bins = list(num)
    for i in range(7):
        if bins[i] == '1':
            ten += 2**(6-i)
    return ten


tmp = input()
n = len(tmp)
nums = []
for i in range(n//7):
    nums.append(tmp[i*7:(i+1)*7])
result = []
for num in nums:
    result.append(bin_to_ten(num))
print(*result)
