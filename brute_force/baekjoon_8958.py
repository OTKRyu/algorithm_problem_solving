tcs = int(input())
result = []
for tc in range(tcs):
    tmp = input()
    sum = 0
    cnum = 0
    for i in range(len(tmp)):
        if tmp[i] == "X":
            cnum = 0
        else:
            cnum += 1
            sum += cnum
    result.append(sum)
for tc in range(tcs):
    print(result[tc])
