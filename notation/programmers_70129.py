def trans(num):
    trans_num=""
    while num:
        trans_num += str(num%2)
        num //= 2
    trans_num = trans_num[::-1]
    return trans_num

def solution(s):
    zeros=0
    count=0
    while 1:
        count += 1
        local_zeros = 0
        for i in range(len(s)):
            if s[i] == "0":
                local_zeros += 1
        zeros += local_zeros
        s = trans(len(s) - local_zeros)
        if s == "1":
            break
        
    answer = [count, zeros]
    return answer