def solution(id_list, reports, k):
    counts = {}
    id_report_list = {}
    for report in reports:
        reporter, reported = report.split(' ')
        if counts.get(reported):
            counts[reported].add(reporter)
        else:
            tmp = set()
            tmp.add(reporter)
            counts[reported] = tmp
        if id_report_list.get(reporter):
            id_report_list[reporter].append(reported)
        else:
            id_report_list[reporter] = [reported]
    answer = []
    for id in id_list:
        if id_report_list.get(id):
            tmps = list(set(id_report_list.get(id)))
            cnt = 0
            for tmp in tmps:
                if counts.get(tmp) and len(counts.get(tmp)) >= k:
                    cnt += 1
            answer.append(cnt)
        else:
            answer.append(0)
        
    return answer