def solution(n):
    inthree = []
    while n > 0:
        inthree.append(n % 3)
        n //= 3
    answer = 0
    for i in range(len(inthree)):
        answer += inthree[i] * (3 ** (len(inthree)-i-1))
    
    return answer