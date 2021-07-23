def my_max(nums):
    m = 0
    for i in range(len(nums)):
        if nums[i] > m:
            m = nums[i]
    return m


for tc in range(1, int(input()) + 1):
    words = []
    cnt = []
    for i in range(5):
        words.append(list((input())))
    for i in range(5):
        cnt.append(len(words[i]))
    tmp = [[0 for i in range(my_max(cnt))] for j in range(5)]
    for i in range(5):
        for j in range(len(words[i])):
            tmp[i][j] = words[i][j]
    result = ''
    for j in range(my_max(cnt)):
        for i in range(5):
            if tmp[i][j]:
                result += tmp[i][j]
    print('#{} {}'.format(tc, result))
