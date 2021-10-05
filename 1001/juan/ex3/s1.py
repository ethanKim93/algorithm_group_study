arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
cnt = 0
for i in range(1, 1 << n):
    my_sum = []
    for j in range(n):                  # n개의 원소와 비교를 할 것
        if i & (1 << j):                # i의 j 번째 비트가 1인 경우(&) j 번째 원소 출력
            my_sum.append(arr[j])
            # print(my_sum[j], end=' ')
    if sum(my_sum) == 0:
        cnt += 1
        print(*my_sum)

print(cnt)