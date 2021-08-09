def r_hanoi(n,i,j):
    if (i==1 and j==2) or (i==2 and j==1):
        k=3
    elif (i==1 and j==3) or (i==3 and j==1):
        k=2
    else:
        k=1
    if n == 1:
        print('{} {}'.format(i,j))
    else:
        r_hanoi(n-1,i,k)
        r_hanoi(1,i,j)
        r_hanoi(n-1,k,j)
def c_hanoi(n):
    if n==1:
        return 1
    else:
        return 2*c_hanoi(n-1) + 1
num = int(input())
print(c_hanoi(num))
r_hanoi(num,1,3)