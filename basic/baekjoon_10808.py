alp_cnt = [0 for i in range(26)]
word = input()
for i in range(len(word)):
    tmp = ord(word[i]) - 97
    alp_cnt[tmp] += 1
print(*alp_cnt)
