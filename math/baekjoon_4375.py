while 1:
    try:
        n = int(input())
        start = '1'
        while 1:
            if int(start) < n:
                start += '1'
            else:
                if int(start)%n ==0:
                    print(len(start))
                    break
                else:
                    start += '1'
    except:
        break