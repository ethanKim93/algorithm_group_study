arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

for i in range(1 << n):
    result = []
    for j in range(n):
        if i & (1 << j):
            result.append(arr[j])
    if sum(result) == 0 and len(result) > 0:
        print(result)