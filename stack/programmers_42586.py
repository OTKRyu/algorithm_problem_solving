def solution(progresses, speeds):
    check = 0 
    answer = []
    while 1:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while check < len(progresses):
            if progresses[check] >= 100:
                cnt += 1
                check += 1
            else:
                break
        if cnt != 0:
            answer.append(cnt)
        if check == len(progresses):
            break
    return answer