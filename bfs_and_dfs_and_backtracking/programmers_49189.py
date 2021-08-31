from collections import deque
def bfs(s, n, adjs):
    check = [0 for i in range(n+1)]
    cnts = [0 for i in range(n)]
    q = deque()
    q.append(s)
    check[s] = 1
    cnts[1] += 1
    while q:
        c = q.popleft()
        for adj in adjs[c]:
            if check[adj] == 0:
                q.append(adj)
                check[adj] = check[c] + 1
                cnts[check[adj]] += 1
    for i in range(1,n):
        if cnts[i] == 0:
            return cnts[i-1]
        
def solution(n, edge):
    adjs = [[] for i in range(n+1)]
    for i in range(len(edge)):
        adjs[edge[i][0]].append(edge[i][1])
        adjs[edge[i][1]].append(edge[i][0]) 
    answer = bfs(1, n, adjs)
    return answer