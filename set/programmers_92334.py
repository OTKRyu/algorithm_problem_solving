def solution(id_list, reports, k):
    reported= {}
    reporter = {}
    for id in id_list:
        reporter[id] = set()
    for report in reports:
        report = report.split(" ")
        reporter[report[0]].add(report[1])
        if reported.get(report[1]):
            reported[report[1]].add(report[0])
        else:
            reported[report[1]] = set()
            reported[report[1]].add(report[0])
    answer = []
    for id in id_list:
        targets = list(reporter[id])
        cnt = 0
        for target in targets:
            if len(reported[target]) >= k:
                cnt += 1
        answer.append(cnt)
    return answer