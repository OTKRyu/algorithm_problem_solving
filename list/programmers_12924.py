def solution(n):
    answer = 0
    for i in range(1,n+1):
        total = 0
        for j in range(1,i+1):
            total += j
        if total == n:
            answer += 1
            continue
        elif total > n:
            break
        else:
            for j in range(1, n-i+1):
                total += j+i
                total -= j
                if total == n:
                    answer += 1
                    break
                elif total > n:
                    break
                    
    return answer