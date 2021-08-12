def per(step):
    if step == m:
        print(*result)
    else:
        if step == 0:
            for i in range(len(nums)):
                if check[nums[i]] != 0:
                    check[nums[i]] -= 1
                    result.append(nums[i])
                    per(step+1)
                    result.pop()
                    check[nums[i]] += 1
        else:
            for i in range(len(nums)):
                if check[nums[i]] != 0 and result[-1] <= nums[i]:
                    check[nums[i]] -= 1
                    result.append(nums[i])
                    per(step+1)
                    result.pop()
                    check[nums[i]] += 1

n, m = map(int, input().split())
nums = list(map(int, input().split()))
check = [0 for i in range(10001)]
for i in range(len(nums)):
    check[nums[i]] += 1
nums = list(set(nums))
nums.sort()
result = []
per(0)
