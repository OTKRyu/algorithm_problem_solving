import sys
sys.setrecursionlimit(10**6)

def get_pre_order(si,ei,sp,ep):
    if ep-sp < 2:
        print(posts[ep], end=' ')
        return
    tmp = 0
    while 1:
        if ins[si+tmp] == posts[ep]:
            break
        else:
            tmp += 1
    print(posts[ep], end=' ')
    get_pre_order(si,si+tmp-1,sp,sp+tmp-1)
    get_pre_order(si+tmp+1,ei,sp+tmp, ep-1)


n = int(input())
ins = list(map(int, input().split()))
posts = list(map(int, input().split()))
get_pre_order(0,n-1,0,n-1)
