def hex_to_bin(num):
    result = ''
    for i in range(len(num)):
        if 48 <= ord(num[i]) < 58:
            tmp = int(num[i])
        else:
            tmp = ord(num[i]) - ord('A') + 10
        result += ten_to_4bin(tmp)
    return result


def ten_to_4bin(num):
    stack = ''
    for i in range(4):
        if num >= 2 ** (3 - i):
            stack += '1'
            num -= 2 ** (3 - i)
        else:
            stack += '0'
    return stack

patterns = {'001101':0,'010011':1,'111011':2,'110001':3,'100011':4,'110111':5,'001011':6,'111101':7,'011001':8,'101111':9}
hexa = input()
tmp = hex_to_bin(hexa)
t = len(tmp)-1
while 1:
    if tmp[t] == '1':
        break
    else:
        t -= 1
ks = []
while 1:
    if t-5 >= 0:
        ks.append(tmp[t-5:t+1])
        t -= 6
    else:
        break
ks.reverse()
result = []
for k in ks:
    result.append(patterns.get(k))
print(*result)