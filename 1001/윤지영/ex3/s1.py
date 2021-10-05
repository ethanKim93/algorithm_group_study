arr = [-1,3,-9,6,7,-6,1,5,4,-2]
n = len(arr)
power_set = [[] for _ in range(1<<n)]
for i in range(1,1<<n):
    for j in range(n):
        if i & (1<<j):
            power_set[i].append(arr[j])
    power_sum = 0
    for p in power_set[i]:
        power_sum += p
    if power_sum == 0:
        print(power_set[i], end=', ')