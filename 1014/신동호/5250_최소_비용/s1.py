import sys
sys.stdin = open('sample_input.txt')

def BFS(i, j):
    q = [(i, j)]
    visited[i][j] = 0
    while q:
        vr, vc = q.pop(0)
        for m in move:
            wr = vr + m[0]
            wc = vc + m[1]
            if wr in range(N) and wc in range(N):
                diff = H[wr][wc] - H[vr][vc]
                if diff < 0:
                    diff = 0
                if visited[wr][wc] > visited[vr][vc] + diff + 1:
                    visited[wr][wc] = visited[vr][vc] + diff + 1
                    q.append((wr, wc))


        
move = ((0, 1), (0, -1), (1, 0), (-1, 0))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [[987654321] * N for _ in range(N)]
    H = [list(map(int, input().split())) for _ in range(N)]
    BFS(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))