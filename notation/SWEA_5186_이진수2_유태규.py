import math

for tc in range(1, 1+int(input())):
    n = float(input())
    result = ''
    for i in range(12):
        if not math.isclose(n,0):
            if n >= (2**(-i-1)):
                result += '1'
                n -= (2**(-i-1))
            else:
                result += '0'
        else:
            print('#{} {}'.format(tc, result))
            break
    else:
        if not math.isclose(n,0):
            print('#{} overflow'.format(tc))
        else:
            print('#{} {}'.format(tc, result))