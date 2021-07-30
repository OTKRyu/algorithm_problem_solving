for tc in range(1, int(input()) + 1):
    student_num = int(input())
    use = [0] * 201
    for i in range(student_num):
        tmp1, tmp2 = map(int, input().split())
        s = (tmp1+1)//2
        e = (tmp2+1)//2
        if s>e:
            s,e = e,s
        for i in range(s, e + 1):
                use[i] += 1
    print('#{} {}'.format(tc, max(use)))
