import sys
sys.stdin = open('sample_input.txt')

di = [-1, 1, 0, 0]  # 상 하 좌 우
dj = [0, 0, -1, 1]

def find_start():
    # 시작점의 좌표 si, sj 구하기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def get_out(i, j):
    Q = [[i, j]]
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while Q:
        ti, tj = Q.pop(0)
        for d in range(4):
            ni = ti + di[d]
            nj = tj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:  # ni, nj 값이 유효하다면
                if maze[ni][nj] == 0 and visited[ni][nj] == 0:  # 다음 지점이 통로라면
                    Q.append([ni, nj])
                    visited[ni][nj] = visited[ti][tj] + 1
                elif maze[ni][nj] == 3:  # 다음 지점이 도착지라면
                    return visited[ti][tj] - 1

    return 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    si, sj = find_start()

    print('#{} {}'.format(test_case, get_out(si, sj)))

