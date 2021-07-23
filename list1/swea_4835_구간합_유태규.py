tcnum = int(input())
for tc in range(1, tcnum + 1):
    length, sm_len = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_sum = 0
    min_sum = 10000*sm_len
    for i in range(length+1-sm_len):
        tmp_sum = 0
        for j in range(sm_len):
            tmp_sum += nums[i+j]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
        if tmp_sum < min_sum:
            min_sum = tmp_sum
    print("#{} {}".format(tc, max_sum-min_sum))
