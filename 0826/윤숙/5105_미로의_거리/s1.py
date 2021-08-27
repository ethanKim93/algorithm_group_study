
def DFS(sx, sy):
    global cnt
    q = [sx, sy] # 큐에 시작지점의 좌표를 넣어줌
    visited[sx][sy] = 1 #시작부분을 방문처리하고 경로를 탐색한다.
    while q: #큐에 있을때 까지 반복. 즉 delta+x 한 경로가 반복해서 찾아가도록 큐에 pop과 append를 반복하며 가능한 경로(0)를 찾아 나간다.
        nowx = q.pop(0) # 시작 경로 x(행) 꺼내기
        nowy = q.pop(0) # 시작 경로 y(열) 꺼내기
        for i in range(4):
            x = nowx + dx[i] #큐에 꺼낸 경로와 델타를 더하며 연산을 (4방향)을 반복한다.
            y = nowy + dy[i]
            if x >= 0 and y >= 0 and x < N and y < N: # 미로의 범위를 벗어나지 않게 가이드라인을 설정해준다.
                if miro[x][y] == 0 and visited[x][y]==0: #미로가 길(0)이고 방문하지 않은 길이면 조건문 실행
                    q.append(x) #현재 경로를 큐에 append를 해준다.
                    q.append(y)
                    visited[x][y]=visited[nowx][nowy]+1 # 시작 경로에서 1로 시작했으므로 이전 방문한 행렬의 값을 더하며 순차적으로 1,2,3,4 탐색해나며 표시를 해준다.

                if miro[x][y] == 3 and visited[x][y]==0: # 도착지점을 찾으면 조건문 실행
                    return  visited[nowx][nowy]-1 #시작경로에 1을 더해주고 시작하므로 1를 빼준다.

    return 0


import sys

sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # print(miro)
    sx = 0
    sy = 0
    cnt = 0
    visited = [[0] * (N) for _ in range(N)] #방문 경로 표시하는 행렬
    for i in range(0, N):
        for j in range(0, N):
            if miro[i][j] == 2:
                sx = i
                sy = j
        if sx and sy:
            break
    dx = [1, -1, 0, 0] #델타 탐색
    dy = [0, 0, -1, 1]
    print('#{} {}'.format(tc,DFS(sx, sy)))
