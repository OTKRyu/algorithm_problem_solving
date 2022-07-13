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


def decode(binary):
    sources = {'211': 0,'221': 1, '122': 2, '411': 3, '132': 4, '231': 5,
               '114': 6, '312': 7, '213': 8, '112': 9}
    codes = []
    tmp = [0, 0, 0]
    flag = 0
    total = 0
    for i in range(len(binary) - 1, -1, -1):
        if len(codes) == 8:
            codes.reverse()
            if valid(codes):
                total += sum(codes)
            codes = []
        else:
            if flag:
                if binary[i] == binary[i + 1]:
                    scnt += 1
                else:
                    lcnt -= 1
                    if lcnt == 0:
                        tmp[lcnt] = scnt
                        # cd = gcd(gcd(tmp[2], tmp[1]), tmp[0])
                        cd = min(tmp)
                        tmp = map(lambda x: x // cd, tmp)
                        tmp = ''.join(map(str, tmp))
                        codes.append(sources.get(tmp))
                        tmp = [0, 0, 0]
                        flag = 0
                    else:
                        tmp[lcnt] = scnt
                        scnt = 1
            else:
                if binary[i] == '1':
                    flag = 1
                    scnt = 1
                    lcnt = 3
    return total

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def valid(nums):
    tmp = 0
    for i in range(8):
        if i % 2:
            tmp += nums[i]
        else:
            tmp += nums[i] * 3
    if tmp % 10:
        return 0
    else:
        return 1


for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    signals = [input() for i in range(n)]
    result = 0
    for i in range(n):
        buff = ''
        flag = 0
        for j in range(m - 1, -1, -1):
            if signals[i][j] == '0':
                buff += signals[i][j]
            else:
                if signals[i][j] != signals[i - 1][j]:
                    flag = 1
                    buff += signals[i][j]
        if flag:
            tmp = hex_to_bin(buff[::-1])
            result += decode(tmp)
    print('#{} {}'.format(tc, result))
