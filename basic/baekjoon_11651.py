from operator import itemgetter

data = []
for tc in range(int(input())):

    x, y = map(int,input().split())
    data.append((x,y))
data.sort(key=itemgetter(1,0))
for i in range(len(data)):
    print(*data[i])