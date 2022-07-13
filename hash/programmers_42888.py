def solution(records):
    uid_to_nickname = {}
    for record in records:
        splited = record.split(" ")
        if splited[0] == "Leave":
            continue
        uid_to_nickname[splited[1]] = splited[2]
    answer = []
    for record in records:
        splited = record.split(" ")
        if splited[0] == "Enter":
            result = f'{uid_to_nickname[splited[1]]}님이 들어왔습니다.'
            answer.append(result)
        elif splited[0] == "Change":
            continue
        else:
            result = f'{uid_to_nickname[splited[1]]}님이 나갔습니다.'
            answer.append(result)
    
    
    return answer