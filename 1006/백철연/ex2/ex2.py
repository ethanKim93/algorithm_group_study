nums = list(range(1,11))
k = 0
lst = []
for i in range(1 << 10):
    subset = []
    for j in range(11):
        if i & (1 << j):
            subset.append(nums[j])
    if sum(subset) == 10:
        lst.append(subset)
print(lst)

