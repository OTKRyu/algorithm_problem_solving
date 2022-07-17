def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        if budget < d[i]:
            answer = i
            break
        else:
            budget -= d[i]
    else:
        answer = len(d)
    return answer