def binary_count(entire, target):
    count = 0
    start = 1
    end = entire
    while start <= end:
        middle = int((start + end) / 2)
        count += 1
        if middle == target:
            return count
        elif middle < target:
            start = middle
        else:
            end = middle


tcs = int(input())
for tc in range(1, tcs + 1):
    tmp = list(map(int, input().split()))
    e_p = tmp[0]
    a_t = tmp[1]
    b_t = tmp[2]
    if binary_count(e_p, a_t) < binary_count(e_p, b_t):
        print('#{} A'.format(tc))
    elif binary_count(e_p, a_t) > binary_count(e_p, b_t):
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
