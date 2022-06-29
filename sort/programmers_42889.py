def solution(N, stages):
    stage_counts = [0 for i in range(N+2)]
    for i in range(len(stages)):
        stage_counts[stages[i]] += 1
    for_sort = []
    total = 0
    for i in range(len(stage_counts)-1, 0, -1):
        if len(stage_counts)-1 == i:
            total += stage_counts[i]
            continue
        total += stage_counts[i]
        if total == 0:
            for_sort.append([0,i])
            continue
        for_sort.append([stage_counts[i]/total, i])
    for_sort.sort(key=lambda x:(-x[0],x[1]))
    answer = []
    for i in range(len(for_sort)):
        answer.append(for_sort[i][1])
    return answer