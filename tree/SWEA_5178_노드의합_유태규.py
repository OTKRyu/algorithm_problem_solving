def postorder(c):
    if 0 < c < n + 1:
        postorder(c * 2)
        postorder(c * 2 + 1)
        if c not in leaf:
            if c * 2 + 1 > n:
                tree[c] = tree[c * 2]
            else:
                tree[c] = tree[c * 2] + tree[c * 2 + 1]


for tc in range(1, 1 + int(input())):
    n, l, tn = map(int, input().split())
    tree = [0] * (n + 1)
    leaf = []
    for i in range(l):
        tmp = list(map(int, input().split()))
        tree[tmp[0]] = tmp[1]
        leaf.append(tmp[0])
    postorder(1)
    print('#{} {}'.format(tc, tree[tn]))
