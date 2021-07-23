def bin_to_ten(num):
    ten = 0
    bins = list(num)
    b= len(bins)
    for i in range(b):
        if bins[i] == '1':
            ten += 2**(b-i-1)
    return ten

def three_to_ten(num):
    ten = 0
    threes = list(num)
    t = len(threes)
    for i in range(t):
        if three[i] == '1':
            ten += 3**(t-i-1)
        elif three[i] == '2':
            ten += (3 ** (t - i - 1))*2
    return ten

for tc in range(1,1+int(input())):
    two = input()
    tw = len(two)
    three = input()
    th = len(three)
    two_possible = []
    two_ten = bin_to_ten(two)
    three_ten = three_to_ten(three)
    for i in range(tw):
        if two[i] == '1':
            two_possible.append(two_ten-2**(tw-i-1))
        else:
            two_possible.append(two_ten+2**(tw-i-1))
    for i in range(th):
        if three[i] == '1':
            tmp = three_ten + 3**(th-i-1)
            if tmp in two_possible:
                result = tmp
                break
            tmp = three_ten - 3**(th-i-1)
            if tmp in two_possible:
                result = tmp
                break
        elif three[i] == '2':
            tmp = three_ten - (3 ** (th - i - 1))*2
            if tmp in two_possible:
                result = tmp
                break
            tmp = three_ten - 3 ** (th - i - 1)
            if tmp in two_possible:
                result = tmp
                break
        else:
            tmp = three_ten + 3 ** (th - i - 1)
            if tmp in two_possible:
                result = tmp
                break
            tmp = three_ten + (3 ** (th - i - 1))*2
            if tmp in two_possible:
                result = tmp
                break
    print('#{} {}'.format(tc, result))

