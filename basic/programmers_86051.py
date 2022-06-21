def solution(numbers):
    checks = [0 for i in range(0,10)]
    for i in range(len(numbers)):
        checks[numbers[i]] =1
    answer = 0
    for i in range(10):
        if checks[i] == 0:
            answer += i
    return answer