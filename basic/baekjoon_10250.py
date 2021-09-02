tcs = int(input())
for tc in range(tcs):
    x, y, o = tuple(map(int, input().split()))
    count = 0
    for i in range(1, y+1):
        for j in range(1, x+1):
            count += 1
            if o == count:
                break
        if o == count:
            break

    if len(str(i)) == 1:
        i = '0' + str(i)
    else:
        i = str(i)
    print(str(j) + i)