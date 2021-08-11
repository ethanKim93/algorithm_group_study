import sys
sys.stdin = open('input.txt')

A = int(input())
for tc in range(1, A + 1):
    N = int(input())
    arr = []
    for _ in range(5):
        arr.append(list(map(int, input().split())))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    result = 0

    for i in range(N):
        esum = 0
        for j in range(N):
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0 <= nx <= 4 and 0 <= ny <= 4:
                    if arr[nx][ny] >= arr[i][j]:
                        esum += arr[nx][ny] - arr[i][j]
                    else:
                        esum += arr[i][j] - arr[nx][ny]
        result += esum
    print('#{} {}'.format(tc, result))