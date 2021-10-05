# 비트연산 풀이
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    if not sum(subset):
        print(subset)