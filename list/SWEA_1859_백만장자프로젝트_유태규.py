for tc in range(1, int(input())+1):
    length = int(input())
    prices = list(map(int, input().split()))
    my = []
    result = 0
    while len(prices) != 0:
        i = prices.index(max(prices))
        for j in range(0,i+1):
            result += prices[i] - prices[j]
        prices = prices[i+1:len(prices)]
    print('#{} {}'.format(tc, result))

