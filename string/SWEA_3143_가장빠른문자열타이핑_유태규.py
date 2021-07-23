for tc in range(1, int(input())+1):
    m, n = input().split()
    cm = []
    match_skip = 0
    for i in range(len(m)):
        if i + len(n) > len(m):
            if match_skip > 0:
                match_skip -= 1
            else:
                cm.append(m[i])
        else:
            if match_skip > 0:
                match_skip -= 1
            else:
                tmp_cnt = 0
                for j in range(len(n)):
                    if m[i+j] == n[j]:
                        tmp_cnt += 1
                if tmp_cnt == len(n):
                    match_skip = len(n) - 1
                    cm.append('*')
                else:
                    cm.append(m[i])
    print('#{} {}'.format(tc, len(cm)))






