n = int(input())
nums = list(map(int, input().split()))
answer = []
for i in range(n):
    answer.append([i, nums[i]])
answer.sort(key=lambda x:x[1])
order = 0
for i in range(n):
    if i == 0:
        answer[i].append(order)
    else:
        if answer[i-1][1] == answer[i][1]:
            answer[i].append(order)
        else:
            order += 1
            answer[i].append(order)
answer.sort(key=lambda x:x[0])
for i in range(n):
    print(answer[i][2], end=' ')