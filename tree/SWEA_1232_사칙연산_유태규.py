def postorder(c):
    global result
    if c != 0:
        postorder(left[c])
        postorder(right[c])
        if c in leafs:
            pass
        else:
            if e[c] == '+':
                e[c] = e[left[c]] + e[right[c]]
            elif e[c] == '-':
                e[c] = e[left[c]] - e[right[c]]
            elif e[c] == '*':
                e[c] = e[left[c]] * e[right[c]]
            elif e[c] == '/':
                e[c] = e[left[c]] / e[right[c]]


for tc in range(1, 11):
    v = int(input())
    e = [0]
    left = [0] * (v + 1)
    right = [0] * (v + 1)
    leafs = []
    for i in range(v):
        tmp = input().split()
        tmpv = int(tmp[0])
        e.append(tmp[1])
        if len(tmp) == 4:
            left[tmpv] = int(tmp[2])
            right[tmpv] = int(tmp[3])
        elif len(tmp) == 3:
            left[tmpv] = int(tmp[2])
        else:
            e[tmpv] = int(e[tmpv])
            leafs.append(tmpv)
    postorder(1)
    print('#{} {}'.format(tc, int(e[1])))
