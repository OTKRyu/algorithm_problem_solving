def isprime(m):
    n = 2 * m
    prime = [False, False] + [True] * (n-1)
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    cnt = 0
    for i in range(m+1, n+1):
        if prime[i] == True:
            cnt += 1
    return cnt


while True:
    num = int(input())
    if num == 0:
        break
    else:
        print(isprime(num))