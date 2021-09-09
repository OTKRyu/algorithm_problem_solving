import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])
    while heap[0] < K:
        if len(heap) == 1 and heap[0] < K:
            return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+2*b)
        answer += 1 
    return answer