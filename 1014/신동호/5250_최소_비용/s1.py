import sys
sys.stdin = open('sample_input.txt')

def BFS(i, j):
    q = [(i, j)]
    # 시작점의 연료 비용은 0
    visited[i][j] = 0
    while q:
        vr, vc = q.pop(0)
        for m in move:
            wr = vr + m[0]
            wc = vc + m[1]
            if wr in range(N) and wc in range(N):
                # diff는 현재 지점 v와 이동할 지점 w의 높이 차
                diff = H[wr][wc] - H[vr][vc] 
                # diff가 음수라면 높이 차로 인한 비용 없음
                if diff < 0:
                    diff = 0
                # 만약 다음 방문할 지점의 과거 비용보다 업데이트될 비용이 싸면 바꿔주고 새롭게 방문한다 
                if visited[wr][wc] > visited[vr][vc] + diff + 1:
                    visited[wr][wc] = visited[vr][vc] + diff + 1
                    q.append((wr, wc))


        
move = ((0, 1), (0, -1), (1, 0), (-1, 0))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [[987654321] * N for _ in range(N)] # 연료 비용 행렬 visited
    H = [list(map(int, input().split())) for _ in range(N)]
    BFS(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))