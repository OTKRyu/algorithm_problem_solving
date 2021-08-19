data = []
for tc in range(int(input())):
     tmp, name = input().split()
     num = int(tmp)
     data.append((num,name))
data.sort(key=lambda x:x[0])
for i in range(len(data)):
    print(*data[i])