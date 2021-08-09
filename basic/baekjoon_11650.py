import sys
from operator import itemgetter, attrgetter

ps = []
for tc in range(int(input())):
    (x,y) = tuple(map(int,sys.stdin.readline().split()))
    ps.append((x,y))

ps.sort(key=itemgetter(0,1))
for i in range(len(ps)):
    print(*ps[i])