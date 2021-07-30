def weird_selection(a):
    for i in range(len(a) - 1):
        if i % 2 != 0:
            t_min = i
            for j in range(i + 1, len(a)):
                if a[t_min] > a[j]:
                    t_min = j
            a[i], a[t_min] = a[t_min], a[i]
        else:
            t_max = i
            for j in range(i + 1, len(a)):
                if a[t_max] < a[j]:
                    t_max = j
            a[i], a[t_max] = a[t_max], a[i]


tcs = int(input())
for tc in range(1, tcs + 1):
    length = int(input())
    nums = list(map(int, input().split()))
    weird_selection(nums)
    result = ' '.join(map(str, nums[:10]))
    print('#{} {}'.format(tc, result))
