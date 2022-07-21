def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    dict1 = {}
    dict2 = {}
    for i in range(len(str1)-1):
        one = str1[i]
        two = str1[i+1]
        if 65 <= ord(one) <= 90 and 65 <= ord(two) <= 90:
            target = one + two
            if dict1.get(target):
                dict1[target] += 1
            else:
                dict1[target] = 1
    for i in range(len(str2)-1):
        one = str2[i]
        two = str2[i+1]
        if 65 <= ord(one) <= 90 and 65 <= ord(two) <= 90:
            target = one + two
            if dict2.get(target):
                dict2[target] += 1
            else:
                dict2[target] = 1
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    finals = list(set1.union(set2))
    n = 0
    u = 0
    for final in finals:
        if dict1.get(final) and dict2.get(final):
            n += min(dict1.get(final),dict2.get(final))
            u += max(dict1.get(final),dict2.get(final))
        else:
            if dict1.get(final):
                u += dict1.get(final)
            if dict2.get(final):
                u += dict2.get(final)
    answer = 0
    if u == 0:
        answer = 65536
    else:
        answer = (n * 65536) // u
    
    return answer