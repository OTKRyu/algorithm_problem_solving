def my_con_count(nums, k):
    count = 0
    for i in range(len(nums)):
        if i == len(nums) - 1:
            if nums[i] == k:
                count += 1
        else:
            if nums[i] == k and nums[i + 1] == 0:
                count += 1
    return count


tcs = int(input())

for tc in range(1, tcs + 1):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    k = tmp[1]
    two_d = []
    count = 0
    for i in range(n):
        two_d.append(list(map(int, input().split())))
    for i in range(n):
        tmp_count = 0
        records = []
        for j in range(n):
            if two_d[i][j] == 0:
                tmp_count = 0
                records.append(tmp_count)
            else:
                tmp_count += 1
                records.append(tmp_count)
        count += my_con_count(records, k)

    for j in range(n):
        tmp_count = 0
        records = []
        for i in range(n):
            if two_d[i][j] == 0:
                tmp_count = 0
                records.append(tmp_count)
            else:
                tmp_count += 1
                records.append(tmp_count)
        count += my_con_count(records, k)
    print('#{} {}'.format(tc, count))
