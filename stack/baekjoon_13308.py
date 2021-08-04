n = int(input())
distances = list(map(int,input().split()))
prices = list(map(int, input().split()))
stack = []
nexts = [-1 for _ in range(n)]

for i in range(len(prices)):
    try:
        while prices[stack[-1]] > prices[i]:
            nexts[stack.pop()] = i
    except:
        pass
    stack.append(i)

start = 0
result = 0
for i in range(n):
    if start != i:
        continue
    else:
        if nexts[i] in [n-1,-1]:
            result += prices[i] * sum(distances[i:n-1])
            break
        else:
            start = nexts[i]
            result += prices[i] * sum(distances[i:nexts[i]])
print(result)