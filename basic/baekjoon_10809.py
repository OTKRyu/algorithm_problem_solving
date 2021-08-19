alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
word = input()
for alp in alps:
    if alp in word:
        print(word.index(alp), end=' ')
    else:
        print(-1, end=' ')