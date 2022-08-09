from collections import deque

def solution(cacheSize, cities):
    q = deque()
    answer = 0
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.appendleft(city)
        else:
            answer += 5
            if cacheSize > 0:
                if len(q) == cacheSize:
                    q.pop()
                    q.appendleft(city)
                else:
                    q.appendleft(city) 
            else:
                continue
            
    return answer