def check(row, col):
    for idx in range(row + 1, N):
        if matrix[idx][col] == 1:
            return 0
        elif matrix[idx][col] == 2:
            return 1
    return 0

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += check(i, j)

    print("#{} {}".format(tc,cnt))