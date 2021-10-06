nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

for i in range(1, 2**len(nums)):
    arr = []
    for j in range(len(nums)):
        if (i >> j) & 1:
            arr.append(nums[j])
    if sum(arr) == 0:
        print(arr)
