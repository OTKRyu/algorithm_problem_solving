def get_cnts(word):
    A_cnt = 0
    a_cnt = 0
    n_cnt = 0
    s_cnt = 0
    for i in range(len(word)):
        if word[i] == ' ':
            s_cnt += 1
        elif 48 <= ord(word[i]) <= 57:
            n_cnt += 1
        elif 65 <= ord(word[i]) <= 90:
            A_cnt += 1
        else:
            a_cnt += 1
    print('{} {} {} {}'.format(a_cnt, A_cnt, n_cnt, s_cnt))

while 1:
    try:
        word = input()
        if not word:
            break
        else:
            get_cnts(word)
    except:
        break