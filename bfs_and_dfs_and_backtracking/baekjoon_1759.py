def dfs(step):
    if step == l:
        vowel_cnt = 0
        consonant_cnt = 0
        for i in range(l):
            if result[i] in ['a','e','i','o','u']:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(result))
        return
    for i in range(c):
        if len(result) == 0:
            result.append(chars[i])
            dfs(step+1)
            result.pop()
        else:
            if result[-1] < chars[i]:
                result.append(chars[i])
                dfs(step+1)
                result.pop()


l, c = map(int, input().split())
result = []
chars = list(input().split())
chars.sort()
dfs(0)