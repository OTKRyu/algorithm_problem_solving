import sys

input = sys.stdin.readline

def per(step):
    global minima
    if step == n:
        total = 0
        if costs[permutation[n-1]][permutation[0]] != 0:
            for i in range(n-1):
                total += costs[permutation[i]][permutation[i+1]]
            total += costs[permutation[n-1]][permutation[0]]
            if minima > total:
                minima = total
    else:
        if permutation:
            for i in range(n):
                if check[i] == 0 and costs[permutation[-1]][i] != 0:
                    permutation.append(i)
                    check[i] = 1
                    per(step+1)
                    check[i] = 0
                    permutation.pop()
        else:
            for i in range(n):
                if check[i] == 0:
                    permutation.append(i)
                    check[i] = 1
                    per(step + 1)
                    check[i] = 0
                    permutation.pop()




n = int(input())
costs = [list(map(int, input().split())) for i in range(n)]
check = [0 for i in range(n)]
permutation = []
minima = 100000001
per(0)
print(minima)