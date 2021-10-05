arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n=len(arr)
lis = []
cnt = -1 #(공집합 빠짐)
for i in range(0, (1 << n)):

    total = 0
    plus = []
    for j in range(0, n):
        if i & (1 << j):
            #print(arr[j], end=' ')
            plus.append(arr[j])
    a = sum(plus)
    if a == 0:
        cnt += 1
        print(plus)
print(cnt)


















