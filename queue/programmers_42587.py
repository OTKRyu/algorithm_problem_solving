from collections import deque

def solution(priorities, location):
    q = deque()
    index_q = deque()
    for i in range(len(priorities)):
        q.append(priorities[i])
        index_q.append(i)
    cnt = 0
    while q:
        c = q.popleft()
        index_c = index_q.popleft()
        if q:
            if max(q) <= c:
                cnt += 1
                if location == index_c:
                    answer = cnt
                    break
            else:
                q.append(c)
                index_q.append(index_c)
        else:
            answer = len(priorities)
            break
    return answer