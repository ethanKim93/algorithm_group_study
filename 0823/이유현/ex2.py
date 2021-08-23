arr = list(range(1, 11))
result = []
for i in range(1<<10):
    p_list = []
    p_sum = 0
    for j in range(10):
        if i & (1<<j):
            p_sum += arr[j]
            p_list.append(arr[j])
    if p_sum == 10:
        result.append(p_list)
print(result)

