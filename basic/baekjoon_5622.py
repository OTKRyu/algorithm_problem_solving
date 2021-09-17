alps = input()
nums = []
for alp in alps:
    if alp in "ABC":
        nums.append(3)
    elif alp in "DEF":
        nums.append(4)
    elif alp in "GHI":
        nums.append(5)
    elif alp in "JKL":
        nums.append(6)
    elif alp in "MNO":
        nums.append(7)
    elif alp in "PQRS":
        nums.append(8)
    elif alp in "TUV":
        nums.append(9)
    elif alp in "WXYZ":
        nums.append(10)
print(sum(nums))

