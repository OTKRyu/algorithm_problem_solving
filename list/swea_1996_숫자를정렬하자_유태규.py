def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


tcs = int(input())
for tc in range(1, tcs+1):
    numlen = int(input())
    nums = list(map(int, input().split()))
    bubble_sort(nums)
    result = " ".join(list(map(str, nums)))
    print("#{} {}".format(tc, result))
