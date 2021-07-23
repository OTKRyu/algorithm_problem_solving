def inorder(v):
    global n, cnt, target, flag
    if v < n+1:
        inorder(v*2)
        if flag:
            cnt += 1
            if target == v:
                flag = 0
        inorder(v*2+1)


for tc in range(1, 1 + int(input())):
    n = int(input())
    target = n // 2
    nums = range(1, n + 1)
    v = n - 1
    l = 1
    lcnt = 0
    rcnt = 0
    length = 1
    while 1:
        for i in range(length):
            lcnt += 1
            v -= 1
            if v == 0:
                break
        if v == 0:
            break
        for i in range(length):
            rcnt += 1
            v -= 1
            if v == 0:
                break
        if v == 0:
            break
        length *= 2
    cnt = 0
    flag = 1
    inorder(1)
    print('#{} {} {}'.format(tc, nums[lcnt], cnt))
