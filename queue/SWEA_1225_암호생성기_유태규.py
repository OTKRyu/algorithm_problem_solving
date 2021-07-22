for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    result = []
    while 1:
        for i in range(1, 6):
            tmp = nums.pop(0)
            tmp -= i
            if tmp <= 0:
                tmp = 0
                nums.append(tmp)
                break
            else:
                nums.append(tmp)
        if nums[-1] == 0:
            break
    final = ' '.join(list(map(str, nums)))
    print('#{}'.format(tc), end=' ')
    print('{}'.format(final))
