arr = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 1, 2, 3, 4]]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def my_abs(a, b):
    if a > b:
        return a - b
    else:
        return b - a


for x in range(len(arr)):
    for y in range(len(arr[x])):
        if x == 0 and y == 0:
            tmpsum = 0
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0 <= tx < len(arr) and 0 <= ty < len(arr[x]):
                    tmpsum += my_abs(arr[x][y], arr[tx][ty])
            maxsum = tmpsum
        else:
            tmpsum = 0
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0 <= tx < len(arr) and 0 <= ty < len(arr[x]):
                    tmpsum += my_abs(arr[x][y], arr[tx][ty])
                if tmpsum > maxsum:
                    maxsum = tmpsum
print(maxsum)