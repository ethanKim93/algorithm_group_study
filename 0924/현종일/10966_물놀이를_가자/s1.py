import sys
from collections import deque
sys.stdin = open("sample_input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    field = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    result = 0
    
    queue = deque()
    for row in range(N):
        for col in range(M):
            if field[row][col] == 'W':
                queue.append((row, col))
                visited[row][col] = 0

    while queue:
        r, c = queue.popleft()
        for arrow in range(4):
            nr, nc = r+dr[arrow], c+dc[arrow]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if field[nr][nc] == 'L' and visited[nr][nc] == -1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                result += visited[nr][nc]


    print("#{} {}".format(tc, result))



