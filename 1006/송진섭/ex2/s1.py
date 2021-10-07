arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
cnt = 0
for i in range(1, 1 << n):
    # cnt += 1
    total = 0
    ans = []
    for j in range(n):
        # cnt += 1
        if i & (1 << j):
            total += arr[j]
            ans.append(arr[j])
            if total > 10:
                break
    if total == 10:
        print(ans)