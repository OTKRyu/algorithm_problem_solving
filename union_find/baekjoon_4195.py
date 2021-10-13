import sys

input = sys.stdin.readline


def union(f1, f2):
    root_f1 = find(f1)
    root_f2 = find(f2)
    if root_f2 != root_f1:
        friends[root_f2][0] = root_f1
        friends[root_f1][1] += friends[root_f2][1]
    return friends[root_f1][1]


def find(f1):
    if f1 == friends[f1][0]:
        return f1
    else:
        friends[f1][0] = find(friends[f1][0])
        return friends[f1][0]


for tc in range(int(input())):
    n = int(input())
    friends = {}
    for i in range(n):
        f1, f2 = input().split()
        if not friends.get(f1):
            friends[f1] = [f1, 1]
        if not friends.get(f2):
            friends[f2] = [f2, 1]
        result = union(f1, f2)
        print(result)
