def solution(n, lost, reserve):
    check = [0 for i in range(n+2)]
    for i in range(len(lost)):
        check[lost[i]] -= 1
    for i in range(len(reserve)):
        check[reserve[i]] += 1
    cnt = 0
    print(check)
    for i in range(1, len(check)-1):
        if check[i] == 1:
            cnt += 1
            if check[i-1] == -1:
                cnt += 1
                check[i-1] += 1
            elif check[i+1] == -1:
                check[i+1] += 1
        elif check[i] == 0:
            cnt += 1
    return cnt