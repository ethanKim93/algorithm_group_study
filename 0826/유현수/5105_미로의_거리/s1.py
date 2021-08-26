import sys
sys.stdin = open('sample_input.txt')


def BFS(start):
    queue.append(start)                                             # 시작점 enQ
    visited[start[0]][start[1]] = 1                                 # 시작점 방문처리
    while queue:                                                    # 큐가 빌 때까지 반복
        now = queue.pop(0)                                          # deQ
        for i in range(4):                                          # 우하좌상 순으로 탐색
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < N:                         # 미로 범위 안쪽인지 확인
                if maze[nr][nc] == '3':                             # 도착지라면 거리 출력
                    return visited[now[0]][now[1]] - 1
                if maze[nr][nc] != '1' and not visited[nr][nc]:     # 벽이 아니고 방문하지 않았다면
                    queue.append((nr, nc))                          # enQ
                    visited[nr][nc] = visited[now[0]][now[1]] + 1   # visited에 거리 입력
    return 0


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    queue = []

    for i in range(N):                                  # 미로를 순회하면서
        for j in range(N):
            if maze[i][j] == '2':                       # 출발점을 찾으면
                print('#{} {}'.format(tc,BFS((i, j))))  # 미로찾기 시작
