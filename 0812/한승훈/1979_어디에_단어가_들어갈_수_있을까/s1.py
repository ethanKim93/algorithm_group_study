import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        x_cnt = y_cnt = 0
        for j in range(N):

            if matrix[i][j]:  # 행
                x_cnt += 1
            if not matrix[i][j] or j == N-1:  # 0이거나 벽에 만났을때
                if x_cnt == K:  # 빈칸이 K개 일때
                    cnt += 1
                x_cnt = 0

            if matrix[j][i]:  # 열
                y_cnt += 1
            if not matrix[j][i] or j == N-1:  # 0이거나 벽에 만났을때
                if y_cnt == K:  # 빈칸이 K개 일때
                    cnt += 1
                y_cnt = 0
    print('#{} {}'.format(tc, cnt))

