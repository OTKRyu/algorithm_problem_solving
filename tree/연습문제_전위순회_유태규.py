def preorder(c):
    if c != 0:
        print(c, end=' ')
        preorder(left[c])
        preorder(right[c])


def inorder(c):
    if c != 0:
        inorder(left[c])
        print(c, end=' ')
        inorder(right[c])


def postorder(c):
    if c != 0:
        postorder(left[c])
        postorder(right[c])
        print(c, end=' ')


v = int(input())
e = list(map(int, input().split()))
left = [0] * (v + 1)
right = [0] * (v + 1)
reverse = [0] * (v + 1)
for i in range(v - 1):
    p, k = e[2 * i], e[2 * i + 1]
    if left[p] == 0:
        left[p] = k
    else:
        right[p] = k
    reverse[k] = p
for i in range(1, v + 1):
    if reverse[i] == 0:
        root = i
postorder(root)
