def solution(answers):
    cnt = 0
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    while cnt < len(answers):
        if answers[cnt] == first[cnt%5]:
            cnt1 += 1
        if answers[cnt] == second[cnt%8]:
            cnt2 += 1
        if answers[cnt] == third[cnt%10]:
            cnt3 += 1
        cnt += 1
    maximum = max(cnt1, cnt2, cnt3)
    answer = []
    if maximum == cnt1:
        answer.append(1)
    if maximum == cnt2:
        answer.append(2)
    if maximum == cnt3:
        answer.append(3)
    return answer