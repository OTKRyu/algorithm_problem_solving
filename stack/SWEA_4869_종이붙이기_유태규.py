for tc in range(1, int(input())+1):
    tmp = int(input())
    num = tmp//10
    for i in range(1,num+1):
        if i ==1:
            result = 1
        else:
            if i%2:
                result *=2
                result -=1
            else:
                result *=2
                result +=1
    print('#{} {}'.format(tc, result))