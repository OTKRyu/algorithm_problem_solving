def solution(numbers, hand):
    key_pad = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2],
        0: [3,1],
    }
    cur_l = [3,0]
    cur_r = [3,2]
    answer = ''
    for number in numbers:
        if key_pad[number][1] == 0:
            answer += "L"
            cur_l = key_pad[number]
        elif key_pad[number][1] == 2:
            answer += "R"
            cur_r = key_pad[number]
        else:
            dis_l = abs(cur_l[0]-key_pad[number][0]) + abs(cur_l[1]-key_pad[number][1])
            dis_r = abs(cur_r[0]-key_pad[number][0]) + abs(cur_r[1]-key_pad[number][1])
            if dis_l < dis_r:
                answer += "L"
                cur_l = key_pad[number]
            elif dis_l > dis_r:
                answer += "R"
                cur_r = key_pad[number]
            else:
                if hand == "right":
                    cur_r = key_pad[number]
                    answer += "R"
                else:
                    cur_l = key_pad[number]
                    answer += "L"

    return answer