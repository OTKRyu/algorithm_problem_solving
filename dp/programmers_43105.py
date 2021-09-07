def solution(triangle):
    copy = [[] for i in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            copy[i].append(triangle[i][j])
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            copy[i+1][j] = max(copy[i][j]+triangle[i+1][j], copy[i+1][j])
            copy[i+1][j+1] = max(copy[i][j]+triangle[i+1][j+1], copy[i+1][j+1])
    answer = max(copy[-1])
    return answer