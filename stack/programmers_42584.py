def solution(prices):
    stack = []
    answer = [len(prices)-i-1 for i in range(len(prices))]

    for i in range(len(prices)):
        try:
            while prices[stack[-1]] > prices[i]:
                tmp = stack.pop()
                answer[tmp] = i - tmp
        except:
            pass
        stack.append(i)
    return answer