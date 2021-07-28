def per(step):
    global maxima, minima, strmax, strmin
    if step == n+1:
        for i in range(n):
            if nonequal[i] == '<':
                if int(permutation[i]) < int(permutation[i+1]):
                    continue
                else:
                    break
            else:
                if int(permutation[i]) > int(permutation[i+1]):
                    continue
                else:
                    break
        else:
            tmp = int(''.join(permutation))
            if maxima < tmp:
                maxima = tmp
                strmax = ''.join(permutation)
            if minima > tmp:
                minima = tmp
                strmin = ''.join(permutation)
    else:
        for i in range(10):
            if check[i] == 0:
                permutation.append(str(i))
                check[i] = 1
                per(step+1)
                check[i] = 0
                permutation.pop()
n = int(input())
nonequal = input().split()
permutation = []
check = [0 for i in range(10)]
maxima = 0
strmax = ''
minima = 10**11
strmin = ''
per(0)
print(strmax)
print(strmin)