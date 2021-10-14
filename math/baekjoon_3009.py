xs =[]
ys = []
result = []
for i in range(3):
    x, y = tuple(map(int, input().split()))
    xs.append(x)
    ys.append(y)
for i in range(3):
    if xs.count(xs[i]) == 1:
        result.append(xs[i])
for i in range(3):
    if ys.count(ys[i]) == 1:
        result.append(ys[i])

print(' '.join(map(str, result)))