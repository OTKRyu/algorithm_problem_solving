def solution(n,a,b):
    answer = 0
    a -= 1
    b -= 1
    while 1:
        answer += 1
        a //= 2
        b //= 2
        if a == b:
            break

    return answer