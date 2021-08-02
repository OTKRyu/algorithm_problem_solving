def per(n,m, cl):
    if len(pers) == m:
        result.append(itr(nums, pers))
        pers.pop()
        return
    else:
        for i in range(4):
            if check[i] > 0:
                pers.append(iters[i])
                check[i] -= 1
                per(n,m, cl+1)
                check[i] += 1
        else:
            if len(pers) != 0:
                pers.pop()
                return
def itr(nums, pers):
    top = 1
    tmp = nums[0]
    for i in range(len(pers)):
        if pers[i] == '+':
            tmp += nums[top]
            top+=1
        elif pers[i] == '-':
            tmp -= nums[top]
            top+=1
        elif pers[i] == '*':
            tmp *= nums[top]
            top+=1
        else:
            if tmp >= 0:
                tmp = tmp//nums[top]
                top+=1
            else:
                tmp *= -1
                tmp = tmp//nums[top]
                tmp *= -1
                top += 1
    return tmp

n = int(input())
nums = list(map(int,input().split()))
check = list(map(int,input().split()))
pers = []
result = []
iters = ['+','-','*','/']
per(n-1,n-1,0)
print(max(result))
print(min(result))