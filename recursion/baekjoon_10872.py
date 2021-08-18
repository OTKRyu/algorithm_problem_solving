def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)
        
num = int(input())
print(fac(num))