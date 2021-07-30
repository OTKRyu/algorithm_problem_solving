def bigger_count(my_list, i):
    count = 0
    for k in range(i+1, len(my_list)):
        if my_list[i] <= my_list[k]:
            count += 1
    return count
for tc in range(1, int(input()) + 1):
    width = (int(input()))
    elements = (list(map(int, input().split())))
    result = 0
    for i in range(width):
        if result < width-1-i-bigger_count(elements, i):
            result = width-i-1-bigger_count(elements, i)
    print("#{} {}".format(tc, result))







