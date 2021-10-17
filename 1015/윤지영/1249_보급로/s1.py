import sys
sys.stdin = open('input.txt')

import collections

def bfs(n):
    que = collections.deque()
    que.append(n)
    arr[n[0]][n[1]] = 0
    while que:
        x,y = que.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0<= nx < N and 0<= ny < N:
                if arr[nx][ny] > arr[x][y] + board[nx][ny]:
                    arr[nx][ny] = arr[x][y] + board[nx][ny]
                    que.append([nx,ny])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input())) for _ in range(N)]
    INF = 987654321
    arr = [[INF] * (N) for _ in range(N)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    bfs([0,0])
    print('#{} {}'.format(tc,arr[N-1][N-1]))


