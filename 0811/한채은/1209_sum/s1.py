import sys
sys.stdin = open('input.txt')

N = 100

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    # 행
    for i in range(N):
        total = 0       # 초기화 시키기(위치 중요)
        for j in range(N):
            total += arr[i][j]
        if max_value < total:
            max_value = total

    # 열
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[j][i]
        if max_value < total:
            max_value = total

    # 대각선(/)
    total = 0
    for i in range(N):
        total += arr[i][N-1-i]  # 인덱스[-i] 보다는 [N-1-i] 권장

        if max_value < total:
            max_value = total

    # 대각선(\)
    total = 0
    for i in range(N):
        total += arr[i][i]

        if max_value < total:
            max_value = total

    print('#{} {}'.format(tc, max_value))



