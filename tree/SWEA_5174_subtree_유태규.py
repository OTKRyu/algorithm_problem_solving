def postorder(c):
    global cnt
    if c != 0:
        postorder(left[c])
        postorder(right[c])
        cnt += 1


for tc in range(1, 1 + int(input())):
    en, n = map(int, input().split())
    v = en + 1
    e = list(map(int, input().split()))
    left = [0] * (v + 1)
    right = [0] * (v + 1)
    reverse = [0] * (v + 1)
    for i in range(v - 1):
        p, k = e[2 * i], e[2 * i + 1]
        if left[p] == 0:
            left[p] = k
        else:
            right[p] = k
    cnt = 0
    postorder(n)
    print('#{} {}'.format(tc, cnt))
