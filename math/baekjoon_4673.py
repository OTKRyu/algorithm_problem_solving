def d(num):
    tmp = map(int, list(str(num)))
    return sum(tmp) + num


dnums = []
for i in range(1, 10001):
    dnums.append(d(i))
    if i not in dnums:
        print(i)
