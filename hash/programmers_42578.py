def solution(clothes):
    hash = dict()
    for i in range(len(clothes)):
        if hash.get(clothes[i][1]):
            hash[clothes[i][1]] += 1
        else:
            hash[clothes[i][1]] = 1
    answer = 1
    for key in hash.keys():
        answer *= (hash[key]+1)
    return answer - 1