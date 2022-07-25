def solution(s):
    tuples = []
    flag = 0
    tmp = []
    tp = []
    for i in range(1, len(s)-1):
        if flag:
            if s[i] == ',':
                tp.append(tmp[:])
                tmp = []
            elif s[i] == '}':
                tp.append(tmp[:])
                tmp = []
                tuples.append(tp[:])
                tp = []
                flag = 0
            else:
                tmp.append(s[i])
        else:
            if s[i] == ',':
                continue
            else:
                flag = 1
    tuples.sort(key=lambda x:len(x))
    result = []
    for tp in tuples:
        tmp = []
        for i in range(len(tp)):
            tmp.append(int(''.join(tp[i])))
        result.append(tmp)
    answer = []
    hashing = {}
    for i in range(len(result)):
        for j in range(len(result[i])):
            if hashing.get(result[i][j]):
                continue
            else:
                answer.append(result[i][j])
                hashing[result[i][j]] = 1
    return answer