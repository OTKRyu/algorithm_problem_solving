def solution(n):
    results = []
    while n != 0:
        if n%3:
            results.append(n%3)
            n //= 3
        else:
            results.append(4)
            n //= 3
            n -= 1
    results.reverse()
    answer = ""
    for result in results:
        answer += str(result)
    return answer