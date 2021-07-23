def inorder(c):
    global result
    if c != 0:
        inorder(left[c])
        result += e[c]
        inorder(right[c])


for tc in range(1, 11):
    v = int(input())
    e = [0] * (v + 1)
    left = [0] * (v + 1)
    right = [0] * (v + 1)
    result = ''
    for i in range(v):
        tmp = input().split()
        tmpv = int(tmp[0])
        e[tmpv] = tmp[1]
        if len(tmp) == 4:
            left[tmpv] = int(tmp[2])
            right[tmpv] = int(tmp[3])
        elif len(tmp) == 3:
            left[tmpv] = int(tmp[2])
    inorder(1)
    print('#{} {}'.format(tc, result))
