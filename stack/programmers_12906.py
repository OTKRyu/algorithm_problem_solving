def solution(arr):
    answer = []
    for num in arr:
        answer.append(num)
        while len(answer) > 1:
            if answer[-2] == answer[-1]:
                answer.pop()
            else:
                break
        
    return answer