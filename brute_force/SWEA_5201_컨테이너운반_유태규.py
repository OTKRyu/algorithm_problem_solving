for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)
    idx = 0
    result = 0
    for truck in trucks:
        while idx < n:
            if weights[idx] <= truck:
                result += weights[idx]
                idx += 1
                break
            else:
                idx += 1
    print('#{} {}'.format(tc, result))
