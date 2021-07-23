def counting_sort(a, k):
    b = [0] * (len(a))
    c = [0] * (k + 1)
    for i in range(0, len(a)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    for i in range(len(b) - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b


stoi = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
itos = {v: k for (k, v) in stoi.items()}

tcs = int(input())
for _ in range(1, tcs + 1):
    tc, length = input().split()
    tmps = input().split()
    nums = []
    for tmp in tmps:
        nums.append(stoi.get(tmp))
    sorted_nums = counting_sort(nums, 9)
    results = [itos.get(sorted_num) for sorted_num in sorted_nums]
    result = ' '.join(results)
    print('{}'.format(tc))
    print('{}'.format(result))
