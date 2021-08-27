import sys
sys.stdin = open('sample_input.txt')


dr = [1, -1, 0, 0]  # 하 상 우 좌
dc = [0, 0, 1, -1]


def move(s_row, s_col):
    q = [[s_row, s_col]]
    visited = list([0] * (N+1) for _ in range(N+1))
    visited[s_row][s_col] = 1
    while q:
        t_row, t_col = q.pop(0)
        for i in range(4):  # 상하좌우 탐색
            nr, nc = t_row + dr[i], t_col + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if miro[nr][nc] == 0 and visited[nr][nc] == 0:
                    q.append([nr, nc])
                    visited[nr][nc] = visited[t_row][t_col] + 1
                elif miro[nr][nc] == 3:  # 목적지 찾을경우
                    return visited[t_row][t_col] - 1
    return 0  # 목적지를 못찾을 경우


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = list(list(map(int, input())) for _ in range(N))
    # print(miro)
    start_row = 0
    start_col = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_row = i
                start_col = j
                break
    ans = move(start_row, start_col)
    print('#{} {}'.format(tc, ans))
