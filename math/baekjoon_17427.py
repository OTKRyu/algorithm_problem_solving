import sys
input = sys.stdin.readline

results = [1 for i in range(1000001)]
for i in range(2, 1000001):
    j = 1
    while i * j < 1000001:
        results[i*j] += i
        j += 1
for i in range(2, 1000001):
    results[i] += results[i-1]
for t in range(int(input())):
    n = int(input())
    print(results[n])