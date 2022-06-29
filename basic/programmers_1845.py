def solution(nums):
    bools = [0 for i in range(200001)]
    count = 0
    for i in range(len(nums)):
        if bools[nums[i]] == 0:
            bools[nums[i]] = 1
            count += 1
            
    answer = 0
    if (len(nums) // 2) < count:
        answer = len(nums) // 2
    else:
        answer = count
    
    return answer