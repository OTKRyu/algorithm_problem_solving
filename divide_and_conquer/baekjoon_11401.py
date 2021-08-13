import sys

input = sys.stdin.readline


def power(a, b):
    if b < 2:
        return a ** b
    else:
        if b % 2:
            return (a * power(a, b // 2) ** 2)%P
        else:
            return (power(a, b // 2) ** 2)%P


P = 1000000007
n, k = map(int, input().split())
fact = [0 for i in range(n + 1)]
for i in range(n + 1):
    if i == 0:
        fact[i] = 1
    else:
        fact[i] = (fact[i - 1] * i) % P
print(((fact[n] * power((fact[k] * fact[n - k]), P - 2)) % P))
