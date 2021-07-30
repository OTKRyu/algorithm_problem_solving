def per(step):
    if step == m:
        print(*permutation)
    else:
        if permutation:
            for i in range(n):
                if check[i] == 0 and permutation[-1] < nums[i]:
                    permutation.append(nums[i])
                    check[i] = 1
                    per(step+1)
                    check[i] = 0
                    permutation.pop()
        else:
            for i in range(n):
                if check[i] == 0:
                    permutation.append(nums[i])
                    check[i] = 1
                    per(step+1)
                    check[i] = 0
                    permutation.pop()



n, m = map(int, input().split())
nums = list(map(int, input().split()))
permutation = []
check = [0 for i in range(n)]
nums.sort()
per(0)