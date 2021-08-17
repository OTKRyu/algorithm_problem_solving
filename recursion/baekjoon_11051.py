def factorial(n,k):
    result = 1
    for i in range(k):
        result *= n-i
    return result
n, k = map(int, input().split())
result = (factorial(n,k)//factorial(k,k))%10007
print(result)