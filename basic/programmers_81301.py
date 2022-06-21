def solution(s):
    letters = list(s)
    answer = []
    num_to_eng = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
        
    }
    for i in range(len(letters)):
        if 48 <= ord(letters[i]) <= 57:
            answer.append(letters[i])
        else:
            for j in range(3,6):
                tmp = ''.join(letters[i:i+j])
                if num_to_eng.get(tmp):
                    answer.append(num_to_eng.get(tmp))
                    break
    answer = ''.join(answer)
    answer = int(answer)
    return answer