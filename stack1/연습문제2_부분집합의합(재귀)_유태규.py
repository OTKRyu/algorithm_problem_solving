ns = [1, 2, 3, 4]
length = len(ns)
c = [0] * length
result = []
cnt = []

def permutation(ns, cl):
    cnt.append(1)
    length = len(ns)
    if cl == length:
        tmp = []
        for i in range(length):
            if c[i]:
                tmp.append(ns[i])
        print(tmp)
    else:
        c[cl] = 1
        permutation(ns, cl + 1)
        c[cl] = 0
        permutation(ns, cl + 1)
# def backper(ns, cl, target):
#     cnt.append(1)
#     length = len(ns)
#     tmp = []
#     if cl == length:
#         return
#     for i in range(length):
#         if c[i]:
#             tmp.append(ns[i])
#     if sum(tmp) == target:
#         result.append(tmp)
#         return
#     elif sum(tmp) > target:
#         return
#     else:
#         c[cl] = 1
#         backper(ns, cl + 1,target)
#         c[cl] = 0
#         backper(ns, cl + 1, target)


permutation(ns, 0)
print(result, sum(cnt))
