tcs = int(input())
for tc in range(1, tcs + 1):
    n = input()
    m = input()

    for i in range(len(m)-len(n)+1):
        cnt = 0
        for j in range(len(n)):
            if m[i + j] == n[j]:
                cnt += 1
        if cnt == len(n):
            print('#{} {}'.format(tc, 1))
            break
    else:
        print('#{} {}'.format(tc, 0))
