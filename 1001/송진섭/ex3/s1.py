num = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(num)
cnt = 0
for i in range(0, (1 << n)):
    total = 0
    for j in range(0, n):
        if i & (1 << j):
            total += num[j]
    if total == 0:
        cnt += 1
print(cnt)