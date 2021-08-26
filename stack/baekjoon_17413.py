word = input()
stack = []
result = ''
flag = 1
for i in range(len(word)):
    if flag:
        if word[i] == '<':
            if stack:
                while stack:
                    result += stack.pop()
            flag = 0
            result += word[i]
        elif word[i] == ' ':
            while stack:
                result += stack.pop()
            result += word[i]
        else:
            stack.append(word[i])
    else:
        if word[i] == '>':
            flag = 1
            result += word[i]
        else:
            result += word[i]
if stack:
    while stack:
        result += stack.pop()
print(result)