def solution(lottos, win_nums):
    answer = []
    lcnt = 0
    zcnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            lcnt += 1
        elif lotto == 0:
            zcnt += 1
    hcnt = zcnt + lcnt
    if 7 - hcnt >= 6:
        answer.append(6)
        answer.append(6)
    else:
        answer.append(7 - hcnt)
        if 7 - lcnt >= 6:
            answer.append(6)
        else:
            answer.append(7 - lcnt)
    
    return answer