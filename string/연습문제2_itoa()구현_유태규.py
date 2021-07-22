def itoa(num):
    value = num
    tmp = []
    while value // 10 != 0:
        tmp.append(chr(ord('0') + (value % 10)))
        value = value // 10
    tmp.append(chr(ord('0') + value))
    result = reverse_back(tmp)
    return ''.join(result)


def reverse_back(chars):
    result = []
    for i in range(len(chars) - 1, -1, -1):
        result.append(chars[i])
    return ''.join(result)


