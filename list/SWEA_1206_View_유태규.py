for test_case in range(1, 11):
    result = 0
    actual_maps = []
    width = int(input())
    building_nums = list(map(int, input().split()))
    for building_num in building_nums:
        building_list = [1 if i < building_num else 0 for i in range(255)]
        actual_maps.append(building_list)
    for j in range(2, width-2):
        for k in range(254, -1, -1):
            if actual_maps[j][k] == 1:
                if actual_maps[j+1][k] == actual_maps[j+2][k] == actual_maps[j-1][k] == actual_maps[j-2][k] == 0:
                    result += 1
                else:
                    break
    print("#{} {}".format(test_case, result))
