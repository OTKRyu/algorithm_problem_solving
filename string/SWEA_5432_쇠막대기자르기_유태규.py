for tc in range(1, int(input()) + 1):
    actual = input()
    result = 0
    tmp_cnt = 0
    for i in range(len(actual)):
        if actual[i] == '(':
            tmp_cnt += 1
            if actual[i+1] != ')':
                result += 1
            else:
                result += (tmp_cnt-1)
        else:
            tmp_cnt -= 1

    print('#{} {}'.format(tc, result))
