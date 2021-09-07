def triplet(cards):
    for i in range(10):
        if cards[i] >= 3:
            return 1
    return 0


def running(cards):
    cnt = 0
    for i in range(10):
        if cards[i] > 0:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            return 1
    return 0


for tc in range(1, 1 + int(input())):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(len(cards)):
        if i % 2:
            player2[cards[i]] += 1
            if running(player2) or triplet(player2):
                print('#{} {}'.format(tc, 2))
                break
        else:
            player1[cards[i]] += 1
            if running(player1) or triplet(player1):
                print('#{} {}'.format(tc, 1))
                break
    else:
        print('#{} {}'.format(tc, 0))