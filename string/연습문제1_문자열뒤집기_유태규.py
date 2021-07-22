def reverse_back(chars):
    result = []
    for i in range(len(chars) - 1, -1, -1):
        result.append(chars[i])
    return ''.join(result)


def reverse_switch(chars):
    result = ['' for i in range(len(chars))]
    if len(chars) % 2 == 0:
        for i in range(len(chars) // 2):
            result[len(chars) - 1 - i] = chars[i]
            result[i] = chars[len(chars) - 1 - i]
        return ''.join(result)
    else:
        for i in range(len(chars) // 2 + 1):
            result[len(chars) - 1 - i] = chars[i]
            result[i] = chars[len(chars) - 1 - i]
        return ''.join(result)


print(reverse_back("apple"))
print(reverse_switch("apple"))
