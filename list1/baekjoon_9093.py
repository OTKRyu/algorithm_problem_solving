for tc in range(int(input())):
    words = input().split()
    for i in range(len(words)):
        print(words[i][::-1], end=' ')
    print()