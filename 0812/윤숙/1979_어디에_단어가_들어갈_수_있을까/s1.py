import sys

sys.stdin = open('input.txt')
T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for i in range(N):

        for j in range(N):
            if arr[i][j] == 0:

                for k in range(4):  # 0 1 2 3
                    cnt = 1
                    for l in range(1, N):  # 0 1 2 3
                        x = i + (l * dx[k])
                        y = j + (l * dy[k])

                        if 0 <= x < N and 0 <= y < N and arr[x][y] == 0:
                            cnt += 1

                    if cnt == K:
                        total += 1


            else:
                continue

    print(total)
