import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        tmp = b
        b = a%b
        a = tmp
    return a

for tc in range(int(input())):
    nums = list(map(int, input().split()))
    total = 0
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            total += gcd(nums[i], nums[j])
    print(total)