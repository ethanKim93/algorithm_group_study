import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]

    N = int(input())

    total = 0   # 겹치는 칸 세주기

    for i in range(1, N+1):
        x1, y1, x2, y2, color = map(int, input().split())

        for x in range(x1, x2+1):   # 처음부터 끝까지
            for y in range(y1, y2+1):
                if color == 1:  # 빨간색이면
                    if arr[x][y] == 0:
                        arr[x][y] = 1  # 색칠하기

                    elif arr[x][y] == 2:    # 파란색이면
                        arr[x][y] = 3   # 보라색으로 칠하기
                        total += 1  # 겹치는 칸 수 셈

                else:   # 파란색이면
                    if arr[x][y] == 0:
                        arr[x][y] = 2   # 파란색으로 칠하기

                    elif arr[x][y] == 1:    # 빨간색이면
                        arr[x][y] = 3       # 보라색으로 칠하기
                        total += 1  # 겹치는 칸 수 세어주기

    print('#{} {}'.format(tc, total))