def solution(new_id):
    answer = new_id.lower()
    answer = list(answer)
    for i in range(len(answer)-1, -1, -1):
        tmp = ord(answer[i])
        if 97 <= tmp <= 122:
            continue
        if 48 <= tmp <= 57:
            continue
        if tmp == 45 or tmp == 46 or tmp == 95:
            continue
        answer.pop(i)
    flag = 0
    newAnswer = []
    for i in range(len(answer)-1,-1,-1):
        if answer[i] == '.':
            if flag:
                continue
            else:
                flag = 1
        else:
            if flag:
                newAnswer.append(".")
                flag = 0
            newAnswer.append(answer[i])
    if flag == 1:
        newAnswer.append(".")
    newAnswer.reverse()
    if len(newAnswer) != 0:
        if newAnswer[0] == ".":
            newAnswer.pop(0)
    if len(newAnswer) != 0:
        if newAnswer[-1] == ".":
            newAnswer.pop()
    if len(newAnswer) == 0:
        newAnswer = "a"
    if len(newAnswer) >= 16:
        newAnswer = newAnswer[0:15]
        if newAnswer[-1] == ".":
            newAnswer.pop()
    while len(newAnswer) <= 2:
        newAnswer += newAnswer[-1]
    newAnswer = "".join(newAnswer)
    return newAnswer