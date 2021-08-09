n, m = map(int, input().split())
q = list(range(1,n+1))
result = []
tmp = [0, 0]
while len(result) != n:
    if q[tmp[1]] != 0:
        if tmp[0] == m-1:
            result.append(q[tmp[1]])
            q[tmp[1]] = 0
        tmp[0] = (tmp[0] +1) % m
    tmp[1] = (tmp[1] + 1) % n
final = ''
for i in range(len(result)):
    if i == len(result)-1:
        final += str(result[i])
    else:
        final += (str(result[i])+', ')
print('<'+final+'>')