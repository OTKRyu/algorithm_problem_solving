for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    pizzas = list(map(int,input().split()))
    n_pizzas = []
    for i in range(m):
        n_pizzas.append([i+1,pizzas[i]])
    queue = []
    while 1:
        while len(queue) != n:
            if n_pizzas:
                queue.append(n_pizzas.pop(0))
            else:
                break
        tmp = queue.pop(0)
        tmp[1] = tmp[1]//2
        if tmp[1]:
            queue.append(tmp)
        if len(queue) == 1:
            break
    print('#{} {}'.format(tc, queue[0][0]))


