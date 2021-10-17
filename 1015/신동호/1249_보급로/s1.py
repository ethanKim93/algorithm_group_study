import sys
sys.stdin = open('input.txt')

def bfs(i, j):
    visited = [[987654321] * N for _ in range(N)]
    visited[i][j] = 0
    q = []
    q.append((i, j))
    while q:
        vr, vc = q.pop(0)
        for m in range(4):
            wr = vr + dr[m]
            wc = vc + dc[m]
            if wr in range(N) and wc in range(N):
                # 기존 경로보다 현재 경로 거치는게 더 빠르다면
                if visited[wr][wc] > visited[vr][vc] + mat[wr][wc]:
                    visited[wr][wc] = visited[vr][vc] + mat[wr][wc]
                    q.append((wr, wc))
    return visited[N-1][N-1]

T = int(input())

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, list(input()))) for _ in range(N)]
    print('#{} {}'.format(tc, bfs(0, 0)))
