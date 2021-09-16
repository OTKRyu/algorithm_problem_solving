w_hs = []
for tc in range(int(input())):
    x, y = map(int, input().split())
    w_hs.append((x, y))
result = []
for w_h1 in w_hs:
    cnt = 0
    for w_h2 in w_hs:
        if w_h1[0] < w_h2[0] and w_h1[1] < w_h2[1]:
            cnt += 1
    result.append(cnt+1)
print(' '.join(map(str,result)))