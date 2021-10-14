nums = []
for i in range(10):
    nums.append(int(input()))
residues = []
for i in range(10):
    residues.append(nums[i]%42)
result = len(set(residues))
print(result)