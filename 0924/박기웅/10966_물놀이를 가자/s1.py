import sys
sys.stdin = open('sample_input.txt')

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pool = [input() for _ in range(N)]
    # 방문 체크 겸 물까지의 최소 거리를 저장하는 2d list
    visited = [[0]*M for _ in range(N)]
    # 선형 큐 정의
    Q = [0] * (N*M)
    front = rear = -1
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                rear += 1
                Q[rear] = (i,j)
    while front != rear:
        front += 1
        i, j = Q[front]
        for w in range(4):
            ni, nj = i+di[w], j+dj[w]
            if 0 <= ni < N and 0 <= nj < M and pool[ni][nj] == 'L':
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    rear += 1
                    Q[rear] = (ni, nj)

    dist = 0
    for i in visited:
        for j in i:
            dist += j

    print('#{} {}'.format(tc, dist))




