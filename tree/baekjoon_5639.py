import sys
sys.setrecursionlimit(10000)

def get_post_order(array):
    if len(array) <= 1:
        return array
    else:
        for i in range(1, len(array)):
            if array[i] > array[0]:
                return get_post_order(array[1:i]) + get_post_order(array[i:]) + [array[0]]
        else:
            return get_post_order(array[1:]) + [array[0]]


nums = []
while 1:
    try:
        nums.append(int(input()))
    except:
        break
results = get_post_order(nums)
for result in results:
    print(result)