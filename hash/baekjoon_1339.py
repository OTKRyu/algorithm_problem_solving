n = int(input())
alpha_cnts = {}
for i in range(n):
    tmp_word = input()
    for j in range(len(tmp_word)):
        if alpha_cnts.get(tmp_word[j]):
            alpha_cnts[tmp_word[j]] += 10 ** (len(tmp_word)-1-j)
        else:
            alpha_cnts[tmp_word[j]] = 10 ** (len(tmp_word)-1-j)
alpha_list = list(alpha_cnts.values())
alpha_list.sort(reverse=True)
result = 0
multi = 9
for alpha in alpha_list:
    result += alpha * multi
    multi -= 1
print(result)
