def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        if i % n > i // n:
            tmp = (i % n) + 1
        else:
            tmp = i // n + 1
        answer.append(tmp)
    
    return answer