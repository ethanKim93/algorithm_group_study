import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]  # 상 하 좌 우

def find_start(spot):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == spot:
                return i, j

def bfs(si, sj):  # 시작점, 도착점
    Q = []
    visited = [[0] * 16 for _ in range(16)]
    visited[si][sj] = 1
    Q.append([si, sj])

    while Q:
        ti, tj = Q.pop(0)
        for d in range(4):
            ni, nj = ti + di[d], tj + dj[d]
            if 0 < ni <= 16 and 0 < nj <= 16:  # ni, nj가 유효할 때
                if maze[ni][nj] == 0 and visited[ni][nj] == 0:  # 길이고, 가보지 않았을 때
                    Q.append([ni, nj])
                    visited[ni][nj] = 1
                elif maze[ni][nj] == 3:  # 다음 지점이 도착할 지점이면
                    return 1

    return 0


for _ in range(10):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 1 벽 # 0 길 # 2 출발점 # 3 도착점

    si, sj = find_start(2)  # 출발점 찾기

    print('#{} {}'.format(test_case, bfs(si, sj)))
