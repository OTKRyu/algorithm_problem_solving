def combination(idx, sidx):
    global result, cnt
    if sidx == m:
        if sum(comb) == s:
            cnt += 1
        return
    if idx == n:
        return
    comb[sidx] = nums[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1,n+1):
    m = i
    comb = [0 for j in range(i)]
    combination(0,0)
print(cnt)