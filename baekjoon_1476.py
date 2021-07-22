import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

i = 1
while 1:
    if i%15 == 0:
        a = 15
    else:
        a = i%15
    if i%28 == 0:
        b = 28
    else:
        b = i%28
    if i%19 == 0:
        c = 19
    else:
        c = i%19
    if a == nums[0] and b == nums[1] and c == nums[2]:
        print(i)
        break
    else:
        i += 1
