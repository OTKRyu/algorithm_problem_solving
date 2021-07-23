for tc in range(1, 1 + int(input())):
    n = int(input())
    usages = [list(map(int, input().split())) for i in range(n)]
    usages.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    end = 0
    for s, e in usages:
        if s >= end:
            ans += 1
            end = e
    print('#{} {}'.format(tc, ans))