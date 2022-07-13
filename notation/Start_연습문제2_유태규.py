def bin_to_ten(num):
    ten = 0
    bins = list(num)
    b = len(bins)
    for i in range(b):
        if bins[i] == '1':
            ten += 2 ** (b - 1 - i)
    return ten


def hex_to_bin(num):
    result = ''
    for i in range(len(num)):
        if 48 <= ord(num[i]) < 58:
            tmp = int(num[i])
        else:
            tmp = ord(num[i]) - ord('A') + 10
        result += ten_to_4bin(tmp)
    return result


def ten_to_4bin(num):
    stack = ''
    for i in range(4):
        if num >= 2 ** (3 - i):
            stack += '1'
            num -= 2 ** (3 - i)
        else:
            stack += '0'
    return stack


hexa = input()
tmps = hex_to_bin(hexa)
if len(tmps)%7:
    n = len(tmps)//7 + 1
else:
    n = len(tmps)//7
bins = []
for i in range(n):
    bins.append(tmps[i * 7:(i + 1) * 7])
result = []
for bin in bins:
    result.append(bin_to_ten(bin))
print(*result)

