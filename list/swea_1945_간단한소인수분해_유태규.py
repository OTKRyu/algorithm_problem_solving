tcs = int(input())
for tc in range(1, tcs+1):
    num = int(input())
    divs = [2, 3, 5, 7, 11]
    counts = []
    for div in divs:
        cnum = num
        count = 0
        stopper = cnum % div
        while stopper == 0:
            cnum = cnum // div
            count += 1
            stopper = cnum % div
        counts.append(count)
    print("#{} {} {} {} {} {}".format(tc, counts[0], counts[1], counts[2], counts[3], counts[4]))
