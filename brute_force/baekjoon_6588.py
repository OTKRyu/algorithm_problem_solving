import sys

input = sys.stdin.readline

prime_check = [1 for i in range(1000001)]
for i in range(2, 100001):
    if prime_check[i] == 1:
        j = 2
        while j * i < 1000001:
            prime_check[j * i] = 0
            j += 1
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(3, n // 2 + 1):
            if i % 2 and prime_check[i] == 1 and prime_check[n - i] == 1:
                print('{} = {} + {}'.format(n, i, n - i))
                break
