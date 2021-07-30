for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    cs = list(map(int, input().split()))
    cs.sort()
    length = max(cs)
    item = 0
    for i in range(len(cs)):
        if (cs[i]//m)*k < i+1:
            print('#{} Impossible'.format(tc))
            break
    else:
        print('#{} Possible'.format(tc))
