def quick(l, r):
    if l < r:
        p = lomuto(l, r)
        quick(l, p - 1)
        quick(p + 1, r)


def lomuto(l, r):
    pivot = r
    i = l - 1
    for j in range(l, r):
        if array[j] <= array[pivot]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[pivot] = array[pivot], array[i + 1]
    return i + 1


def hoare(l, r):
    pivot = l
    i = l + 1
    j = r
    while i <= j:
        if array[i] > array[pivot] and array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] > array[pivot]:
            j -= 1
        elif array[pivot] >= array[j]:
            i += 1
        else:
            i += 1
            j -= 1
    array[pivot], array[j] = array[j], array[pivot]
    return j


for tc in range(1, 1 + int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    # quick(0, n - 1) quick정렬 했는데 시간초과 나서 뭘 더 줄여야될지 모르겠음
    array.sort()
    print('#{} {}'.format(tc, array[n // 2]))
