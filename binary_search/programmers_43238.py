def solution(n, times):
    left = 1
    right = n * max(times)
    while left <= right:
        mid = (left+right)//2
        tmp = 0
        for i in range(len(times)):
            tmp += mid//times[i]
        if tmp < n:
            left = mid +1
        else:
            right = mid -1
    return left