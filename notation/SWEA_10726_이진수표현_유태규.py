def ten_to_bin(num):
    k = 27
    result = ''
    for i in range(k+1):
        if num >= 2**(k-i):
            num -= 2**(k-i)
            result += '1'
        else:
            result += '0'
    return result

for tc in range(1,1+int(input())):
    n, m = map(int, input().split())
    tmp = ten_to_bin(m)
    flag = 1
    for i in range(n):
        if tmp[-1-i] != '1':
            flag = 0
            break
    if flag:
        answer = 'ON'
    else:
        answer = 'OFF'
    print('#{} {}'.format(tc, answer))
