def selection_sort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]


tcs = int(input())
for tc in range(1, tcs + 1):
    length = int(input())
    nums = list(map(int, input().split()))
    selection_sort(nums)
    result = ' '.join(map(str, nums))
    print('#{} {}'.format(tc, result))
