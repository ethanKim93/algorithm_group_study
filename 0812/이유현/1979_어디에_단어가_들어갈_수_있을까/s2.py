N, K = 5, 3

arr = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]

result = 0
i = 0
while i <= N-1:
    cnt1 = 0
    for num in arr[i]:
        if num == 1:
            cnt1 += 1
    if cnt1 == 3:
        for j in range(N-K+1):
            blank = arr[i][j:j+K]
            print(blank)
            # if 0 not in blank:
            #     result += 1
        i += 1
    else:
        i += 1

