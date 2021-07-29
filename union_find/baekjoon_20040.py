import sys

input = sys.stdin.readline


def find(x):
    stack = [x]
    flag = 1
    while stack:
        if flag:
            if stack[-1] == readers[stack[-1]]:
                result = stack.pop()
                flag = 0
            else:
                stack.append(readers[stack[-1]])
        else:
            readers[stack.pop()] = result
    return result


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return 0
    else:
        readers[root_y] = root_x
        return 1


n, m = map(int, input().split())
readers = list(range(n))
flag = 1
for i in range(m):
    v1, v2 = map(int, input().split())
    if flag:
        if union(v1, v2):
            continue
        else:
            print(i+1)
            flag = 0
if flag:
    print(0)
