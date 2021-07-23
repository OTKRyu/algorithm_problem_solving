def search(target, nums):
    s = 0
    e = len(nums) - 1
    flag = 0
    cross = ''
    while e - s > -1:
        m = (e + s) // 2
        if target == nums[m]:
            flag = 1
            break
        elif target > nums[m]:
            s = m + 1
            cross += 'r'
        else:
            e = m - 1
            cross += 'l'
    if flag:
        if len(cross) <= 1:
            return 1
        else:
            flag2 = 1
            for i in range(len(cross) - 1):
                if cross[i] == cross[i + 1]:
                    flag2 = 0
                    break
            if flag2:
                return 1


for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bs = list(map(int, input().split()))
    cnt = 0
    for b in bs:
        if search(b, a):
            cnt += 1
    print('#{} {}'.format(tc, cnt))
