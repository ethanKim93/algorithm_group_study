import sys
sys.stdin = open('input.txt')
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(5):
        arr.append(list(map(int, input().split())))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    answer = 0

    for i in range(5):
        element_sum = 0
        for j in range(5):
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0 <= nx <= 4 and 0 <= ny <= 4:
                    if arr[nx][ny] >= arr[i][j]:
                        element_sum += arr[nx][ny] - arr[i][j]
                    else:
                        element_sum += arr[i][j] - arr[nx][ny]
        answer += element_sum
    print('#{} {}'.format(tc, answer))