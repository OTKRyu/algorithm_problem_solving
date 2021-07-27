n = int(input())
len_n = len(str(n))
cnts = [9 * 10**(i) for i in range(0, len_n)]
total = 0
for i in range(len(cnts)):
    if i == len(cnts)-1:
        total += (i+1) * (n-sum(cnts[:-1]))
    else:
        total += (i+1) * cnts[i]
print(total)