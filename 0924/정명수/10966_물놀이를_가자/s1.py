import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    answer = [[0]*M for _ in range(N)]
    water = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                answer[i][j] = 0
                water.append([i,j])
            elif arr[i][j] == 'L':
                answer[i][j] = 1000
    ans = 0
    while water:
        w = water.popleft()
        for i in range(4):
            nr = dx[i]+w[0]
            nc = dy[i]+w[1]
            if 0 <= nr < N and 0 <= nc < M:
                k = answer[w[0]][w[1]] + 1
                if answer[nr][nc] and answer[nr][nc] > k:
                    answer[nr][nc] = k
                    water.append((nr,nc))
    for i in range(N):
        for j in range(M):
            ans += answer[i][j]

    print('#{} {}'.format(tc,ans))


