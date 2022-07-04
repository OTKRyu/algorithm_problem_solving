def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += i
    for i in range(1,32):
        if left <= i * i <= right:
            answer -= i*i*2
            
    return answer