from pprint import pprint
import sys
sys.stdin = open("input.txt")

def bfs(e):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = []

    i, j = e[0], e[1]  # 시작지점
    q.append([i,j])
    while q: #안비면 트루
        i,j = q.pop(0)
        for k in range(4):
            ni = i + di[k] #방향 지정해서 새로운 좌표
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:  # 범위 내 이고 0이면
                if visited[ni][nj] == 0: #갔던곳 다시 안감
                    if arr[ni][nj] == 2:
                        return visited[i][j]
                    elif arr[ni][nj] == 0:
                        q.append([ni,nj]) #1.1로 이동
                        # visited[ni][nj] = 1 #돌아갈 필요 없을때
                        visited[ni][nj] = visited[i][j] + 1 #위치갈때마다 +1
        pprint(visited)
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                e = (i, j)

    visited = [[0]*N for _ in range(N)]
    print(bfs(e))