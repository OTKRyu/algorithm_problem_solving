def row_sum(two_d, i):
    total = 0
    for num in two_d[i]:
        total += num
    return total


def col_sum(two_d, j):
    total = 0
    for i in range(len(two_d)):
        total += two_d[i][j]
    return total


for test_case in range(1, 11):
    tc = int(input())
    actual = []
    row_max = 0
    col_max = 0
    diag_max = 0
    true_max = 0
    for i in range(100):
        actual.append(list(map(int, input().split())))
    for i in range(100):
        if row_sum(actual, i) > row_max:
            row_max = row_sum(actual, i)
    for j in range(100):
        if col_sum(actual, j) > row_max:
            row_max = col_sum(actual, j)
    for k in range(100):
        diag_max += actual[k][99 - k]
    tmp_sum = 0
    for k in range(100):
        tmp_sum += actual[k][k]
    if diag_max < tmp_sum:
        diag_max = tmp_sum
    true_max = row_max
    if true_max < col_max:
        true_max = col_max
    if true_max < diag_max:
        true_max = diag_max
    print("#{} {}".format(tc, true_max))
