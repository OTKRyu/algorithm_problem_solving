iron_bar = input()
stack = 0
total = 0
for i in range(len(iron_bar)):
    if iron_bar[i] == '(':
        stack += 1
    else:
        if iron_bar[i-1] == '(':
            total += stack-1
            stack -= 1
        else:
            total += 1
            stack -= 1
print(total)