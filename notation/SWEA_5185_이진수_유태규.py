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

for tc in range(1,1+int(input())):
    tmp = input().split()
    result = hex_to_bin(tmp[1])
    print('#{} {}'.format(tc, result))
