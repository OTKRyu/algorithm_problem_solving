def solution(participant, completion):
    answer = ""
    dict_ptcp = {}
    dict_cpl = {}
    for person in participant:
        if dict_ptcp.get(person) == None:
            dict_ptcp[person] = 1
        else:
            dict_ptcp[person] += 1
    for person in completion:
        if dict_cpl.get(person) == None:
            dict_cpl[person] = 1
        else:
            dict_cpl[person] += 1
    for person in participant:
        if dict_cpl.get(person) != dict_ptcp.get(person):
            answer = person
    return answer